

可以使用Streamlit，这是一个用于快速构建和共享数据应用的库。

以下是一个简化的示例，允许用户上传`.xlsx`文件并生成`.json`文件：

### 安装Streamlit

首先，确保你已经安装了Streamlit和pandas库。如果没有安装，可以使用以下命令进行安装：

```sh
pip install streamlit -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 创建Streamlit应用程序

创建一个新的Python脚本文件（例如`app.py`）并添加以下代码：

```python
import streamlit as st
import pandas as pd

st.title('Excel to JSON Converter')

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Excel file content:")
    st.write(df)
    
    json_data = df.to_json(orient='records', force_ascii=False)

    st.download_button(
        label="Download JSON",
        data=json_data,
        file_name='data.json',
        mime='application/json'
    )
```

### 运行Streamlit应用程序

在终端或命令行中，导航到包含`app.py`的目录，并运行以下命令启动Streamlit应用程序：

```sh
python -m streamlit run app.py
```

然后打开浏览器，访问Streamlit提供的本地URL（通常是`http://localhost:8501/`或`http://127.0.0.1:8501/`），你应该会看到一个简单的页面，允许你上传`.xlsx`文件并下载生成的`.json`文件。
