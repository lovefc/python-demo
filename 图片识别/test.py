# coding: utf-8
import pytesseract
from PIL import Image

# 设置 Tesseract OCR 的安装路径（如果它不在系统默认路径中）
# 这里是windows下的路径，linux默认安装的话，不需要这行，直接去掉这行
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 打开图像文件
image_path = 'test.png'

img = Image.open(image_path)

# 使用 Tesseract 进行文字识别
text = pytesseract.image_to_string(img,lang='chi_sim')

# 打印识别的文字
print(text);