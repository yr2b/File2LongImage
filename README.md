# File2LongImage
# 文件转长图工具

## 简介
这个工具是一个用于将多种文件格式（如 PDF、Word、Excel、PPT 等）转换为长图片的工具。通过该工具，你可以上传一个文件，工具会自动将其转换为 PDF 并生成一张合并后的长图。这个项目使用 [Streamlit](https://streamlit.io/) 作为前端展示界面，使用 [pdf2image](https://github.com/Belval/pdf2image) 进行 PDF 到图片的转换，并使用 [Pillow](https://python-pillow.org/) 来处理图片的合并。

## 功能
- 支持多种文件格式：PDF、Word、Excel、PPT 等。
- 将文件转换为 PDF 并自动转换为图片。
- 合并多张图片为长图，便于查看和分享。
- 可设置图片的 DPI（PPI）以调整输出图片的质量。

## 依赖环境
要运行此项目，请确保已安装以下依赖：
- [Streamlit](https://streamlit.io/)：用于构建交互式 Web 应用程序。
- [pdf2image](https://github.com/Belval/pdf2image)：将 PDF 转换为图像的库。
- [Pillow](https://python-pillow.org/)：图像处理库。
- [poppler-utils](https://poppler.freedesktop.org/)：用于支持 PDF 转换的工具。

### 如不熟悉配置流程，也可直接下载打包好的文件运行，基于tkinter，所以页面不如streamlit精美
### 环境及可执行文件下载地址：

#### [夸克盘](https://pan.quark.cn/s/a5d0e37115a8)

#### [百度盘,提取码69hi](https://pan.baidu.com/s/1p6reebYtEnxt0od-BxIxyQ?pwd=69hi)

## 安装步骤
1. 克隆项目到本地：
    ```bash
    git clone https://github.com/你的用户名/文件转长图工具.git
    cd 文件转长图工具
    ```

2. 安装所需的 Python 库：
    ```bash
    pip install -r requirements.txt
    ```

3. 安装 Poppler：
   - **Windows**: 下载 [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)，并将其路径添加到系统环境变量，或者在 `config.py` 中设置 `POPPLER_PATH`。
   - **macOS**: 使用 Homebrew 安装：
     ```bash
     brew install poppler
     ```
     并在 `config.py` 中设置 `POPPLER_PATH`，如 `/usr/local/bin`。
   - **Linux**: 使用包管理器安装（以 Ubuntu 为例）：
     ```bash
     sudo apt-get install poppler-utils
     ```
     并在 `config.py` 中设置 `POPPLER_PATH`，如 `/usr/bin`。

4. 安装 LibreOffice（如果需要转换非 PDF 文件，如 Word、Excel、PPT）：
   - **Windows**: 下载并安装 [LibreOffice](https://www.libreoffice.org/download/download/)，并在 `config.py` 中设置 `LIBREOFFICE_PATH`。
   - **Linux**/ **macOS**:
     ```bash
     sudo apt install libreoffice
     ```
     并在 `config.py` 中设置 `LIBREOFFICE_PATH`，如 `/usr/bin/libreoffice`。

5. 配置文件
   - 编辑 `config.py` 文件，设置以下参数：
     - `OUTPUT_DIR`: 输出目录的路径。
     - `POPPLER_PATH`: Poppler 的安装路径。
     - `LIBREOFFICE_PATH`: LibreOffice 的安装路径。

## 运行方法
1. 在项目目录下运行以下命令启动应用：
    ```bash
    streamlit run main.py
    ```

2. 打开浏览器并访问 `http://localhost:8501`，即可看到应用界面。

3. 上传需要转换的文件，并设置图片 DPI。等待文件转换完成后，页面将展示合并后的长图。



## 文件说明
- `main.py`: 主程序文件，处理文件上传、格式转换和图像合并等功能。
- `requirements.txt`: 项目所需的依赖库清单。
- `config.py`: 配置文件，包含所有的目录配置。
- `run_app.py`: 运行此py文件可直接运行程序
- `TKGUI.py`: 使用tkinter重新构建的程序，不通过网页运行，更方便打包和本地使用。
  
## 注意事项
- **系统支持**：目前仅在windows下进行过测试，其他系统环境可能需要自行适配
- **文件大小**：请注意上传文件的大小，因为转换和合并较大的文件可能会耗费较长时间。
- **格式支持**：该工具依赖 LibreOffice 进行非 PDF 文件的转换，因此确保安装了正确版本的 LibreOffice。
- **图片质量**：通过调整 DPI 来控制输出图片的质量，DPI 越高，图片越清晰，但文件大小也会增大。

## 以上readme文件主要由o1生成，如有错误，请指出

## 开源许可
该项目基于 MIT 开源许可进行分发。详情请查看 [LICENSE](LICENSE)。
