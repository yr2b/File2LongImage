import os
import sys
import time
import subprocess
import pdf2image
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def merge_images(images, output_path, progress_var, status_label):
    status_label.config(text="开始合并图像...")
    progress_var.set(0)
    root.update_idletasks()
    start_time = time.time()

    widths, heights = zip(*(i.size for i in images))
    total_height = sum(heights)
    max_width = max(widths)

    merged_image = Image.new('RGB', (max_width, total_height))
    y_offset = 0

    total_images = len(images)
    for idx, img in enumerate(images):
        merged_image.paste(img, (0, y_offset))
        y_offset += img.height

        # 更新进度
        progress = (idx + 1) / total_images * 100
        progress_var.set(progress)
        elapsed_time = time.time() - start_time
        estimated_total_time = elapsed_time / ((idx + 1) / total_images)
        remaining_time = estimated_total_time - elapsed_time
        status_label.config(text=f"正在合并图像：{idx + 1}/{total_images}，预计剩余时间：{int(remaining_time)}秒")
        root.update_idletasks()

    merged_image.save(output_path)
    status_label.config(text="图像合并完成！")
    progress_var.set(100)
    root.update_idletasks()
    os.startfile(output_path)  # 仅适用于 Windows

def convert_to_image(file_path, output_dir, dpi, progress_var, status_label):
    status_label.config(text="开始转换文件...")
    progress_var.set(0)
    root.update_idletasks()
    start_time = time.time()

    images = []
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    if file_path.lower().endswith('.pdf'):
        poppler_path = os.path.join("poppler", "poppler-24.07.0", "Library", "bin")
        images = pdf2image.convert_from_path(file_path, poppler_path=poppler_path, dpi=dpi)
        progress_var.set(30)
        root.update_idletasks()
    elif file_path.lower().endswith((".doc", ".docx", ".ppt", ".pptx", ".csv", ".xls", ".xlsx", ".odt", ".rtf", ".txt", ".psd", ".cdr", ".wps", ".svg")):
        if sys.platform.startswith('win'):
            libreoffice_path = os.path.join('.', 'libreoffice', 'App', 'libreoffice', 'program', 'soffice.exe')
        else:
            libreoffice_path = os.path.join('.', 'LibreOffice-fresh.basic-x86_64.AppImage')

        pdf_path = os.path.join(output_dir, f"{base_name}.pdf")
        if sys.platform.startswith('win'):
            conversion_cmd = f'"{libreoffice_path}" --headless --convert-to pdf "{file_path}" --outdir "{output_dir}"'
        else:
            conversion_cmd = f'{libreoffice_path} --headless --convert-to pdf "{file_path}" --outdir "{output_dir}"'
        subprocess.run(conversion_cmd, shell=True)

        if not os.path.exists(pdf_path):
            messagebox.showerror("错误", "文件转换为 PDF 失败")
            return
        else:
            status_label.config(text=f"文件转换为 PDF 成功，正在转换为图像: {pdf_path}")
            progress_var.set(60)
            root.update_idletasks()

        poppler_path = os.path.join("poppler", "poppler-24.07.0", "Library", "bin")
        images = pdf2image.convert_from_path(pdf_path, poppler_path=poppler_path, dpi=dpi)
        progress_var.set(90)
        root.update_idletasks()
    else:
        messagebox.showerror("错误", "不支持的文件格式")
        return

    if images:
        merged_output_path = os.path.join(output_dir, f"{base_name}.png")
        merge_images(images, merged_output_path, progress_var, status_label)
        progress_var.set(100)
        status_label.config(text="文件转换完成！")
        root.update_idletasks()
        messagebox.showinfo("成功", f"文件已成功转换并保存为：{merged_output_path}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("所有支持的文件", "*.pdf;*.doc;*.docx;*.ppt;*.pptx;*.csv;*.xls;*.xlsx;*.odt;*.rtf;*.txt;*.psd;*.cdr;*.wps;*.svg")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def start_conversion():
    file_path = file_entry.get()
    dpi = int(dpi_entry.get())
    if not file_path:
        messagebox.showwarning("警告", "请选择一个文件")
        return
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    convert_to_image(file_path, output_dir, dpi, progress_var, status_label)

root = tk.Tk()
root.title("文件转长图工具")

frame = tk.Frame(root)
frame.pack(pady=10)

file_label = tk.Label(frame, text="选择文件：")
file_label.grid(row=0, column=0, padx=5, pady=5)

file_entry = tk.Entry(frame, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)

file_button = tk.Button(frame, text="浏览", command=select_file)
file_button.grid(row=0, column=2, padx=5, pady=5)

dpi_label = tk.Label(frame, text="设置图片 PPI：")
dpi_label.grid(row=1, column=0, padx=5, pady=5)

dpi_entry = tk.Entry(frame)
dpi_entry.insert(0, "300")
dpi_entry.grid(row=1, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="开始转换", command=start_conversion)
start_button.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=20, pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()