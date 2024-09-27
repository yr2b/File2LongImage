import sys
import os

# 输出目录
OUTPUT_DIR = "output"

# Poppler 路径
if sys.platform.startswith('win'):
    POPPLER_PATH = os.path.join("poppler", "poppler-24.07.0", "Library", "bin")
    # 默认poppler路径是当前目录
else:
    POPPLER_PATH = "/usr/bin"  # 根据实际安装路径修改

# LibreOffice 路径
if sys.platform.startswith('win'):
    LIBREOFFICE_PATH = os.path.join('.', 'libreoffice', 'App', 'libreoffice', 'program', 'soffice.exe')
    # 默认libreoffice路径是当前目录
else:
    LIBREOFFICE_PATH = "/usr/bin/libreoffice"  # 根据实际安装路径修改