# PDF 文件翻译脚本

本文档为您提供使用指南和背景信息，帮助您有效使用 PDF 文件翻译脚本。
该脚本使用 Google 的 Gemini API 来翻译 PDF 文件中的文本，并支持将翻译结果输出为文本文件。

## 功能描述

该脚本能够：

- 从 PDF 文件中提取文本。
- 使用 Google Gemini API 对提取的文本进行翻译。
- 输出翻译后的文本，支持输出原文和翻译文本或仅翻译文本。

## 系统要求

Python 3.7 或更高版本。
安装 requirements.txt 中指定的库。

## 安装依赖

在运行脚本前，请确保已安装所有必需的依赖。可以通过以下命令安装：

`pip install -r requirements.txt`


## 配置文件

您需要创建一个名为 settings.cfg 的配置文件，该文件应包含以下内容：

[option]
google-apikey = your_gemini_api_key
prompt = Please translate the following text into Chinese:
bilingual-output = True
langcode = en
google-apikey: 您的 Google Gemini API 密钥。
prompt: 翻译提示语，指示翻译的目标语言。
bilingual-output: 是否输出原文和翻译文本。设置为 True 或 False。
langcode: 输出文件的语言代码。

## 运行脚本

使用以下命令行语法运行脚本：

`python geminiTrans.py <path_to_pdf_file>`

其中 <path_to_pdf_file> 是您希望翻译的 PDF 文件的路径。

## 输出

脚本将在同一目录下生成一个与 PDF 同名但带有 _translated.txt 后缀的文件，包含翻译后的文本。

## 错误处理

如果在翻译过程中遇到 API 配额限制错误，脚本会尝试等待后重试。其他类型的错误将会被记录并显示在控制台。

## 安全和隐私

请确保您的 API 密钥存放安全，避免泄露。处理的 PDF 文件和生成的翻译文本应根据需要保护隐私和数据安全。

## 支持

如果您在使用脚本时遇到任何问题，可以通过查看 Gemini API 文档来获取更多帮助，或者联系技术支持。

## 许可证

该脚本遵循 MIT 许可证。在使用脚本前，请确保您已阅读并同意相关的使用条款和条件。
