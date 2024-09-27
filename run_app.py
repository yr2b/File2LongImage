import streamlit.web.cli as stcli  # 修改了导入模块
import sys

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "main.py"]
    sys.exit(stcli.main())