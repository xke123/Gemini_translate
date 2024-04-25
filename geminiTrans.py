import os
import argparse
import configparser
import pdfminer.high_level
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
import google.generativeai as genai

# 读取配置文件
config = configparser.ConfigParser()
config.read('settings.cfg')
api_key = config['option']['google-apikey']
prompt = config['option']['prompt']
bilingual_output = config.getboolean('option', 'bilingual-output', fallback=True)
lang_code = config['option']['langcode']
max_characters = 1000  # 根据 API 的限制设置，适当调整

# 配置并加载 API
genai.configure(api_key=api_key)

# 初始化 Gemini 模型
model = genai.GenerativeModel('gemini-1.0-pro-latest')

# 翻译函数
def translate_text(text):
    if len(text) <= max_characters:
        # 文本长度小于最大字符限制，直接翻译
        response = model.generate_content(f"{prompt} {text}")
        if response.parts:
            return response.text
        else:
            return "Translation failed due to content safety restrictions."
    else:
        # 文本超出字符限制，需要分割后翻译
        parts = [text[i:i + max_characters] for i in range(0, len(text), max_characters)]
        translated_parts = []
        for part in parts:
            if part.strip():
                response = model.generate_content(f"{prompt} {part}")
                if response.parts:
                    translated_parts.append(response.text)
                else:
                    translated_parts.append("Part translation failed due to content safety restrictions.")
        return " ".join(translated_parts)

# 主函数，处理命令行输入的 PDF 文件
def main():
    parser = argparse.ArgumentParser(description='Translate text from a PDF document.')
    parser.add_argument('filename', help='Name of the PDF file')
    args = parser.parse_args()

    output_file = f"{os.path.splitext(args.filename)[0]}_translated.txt"
    with open(args.filename, 'rb') as f:
        parser = PDFParser(f)
        document = PDFDocument(parser)

        with open(output_file, 'w', encoding='utf-8') as out_file:
            for page_number, page in enumerate(PDFPage.create_pages(document), 1):
                page_text = pdfminer.high_level.extract_text(f, page_numbers=[page_number - 1])
                if not page_text.strip():
                    continue  # 跳过空白页
                translated_text = translate_text(page_text)
                if bilingual_output:
                    out_file.write(f"Page {page_number} - Original:\n{page_text}\n\n")
                    out_file.write(f"Page {page_number} - Translated:\n{translated_text}\n\n")
                else:
                    out_file.write(f"Page {page_number} - Translated:\n{translated_text}\n\n")
                print(f"Translated page {page_number}")

    print(f"Translation completed and saved to {output_file}")

if __name__ == '__main__':
    main()
