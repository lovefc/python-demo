## 利用pytesseract来识别图片

## windows

python版本：3.8.5

1.首先要安装pytesseract扩展

`pip install pytesseract`


2.安装tesseract

github上的源码需要自己编译，这里提供一下已编译好的exe包，直接下载使用。

https://digi.bib.uni-mannheim.de/tesseract/

选择对应版本，安装即可，记住路径，这个在代码中是要填写的，语言包安装的时候也要用到。

`# 设置 Tesseract OCR 的安装路径（如果它不在系统默认路径中）`
`pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`

3.安装语言包

默认是不能识别中文的，必须要下载中文语言包。

打开github仓库：https://github.com/tesseract-ocr/tessdata

`chi_sim.traineddata`就是中文语言包，下载之后，放到tesseract的安装路径下的`tessdata`目录下。

4.运行`py test.py`代码，应该就能看到识别内容了。

## linux

python版本：3.8.10

1.首先要安装pytesseract扩展

`pip install pytesseract`

2.安装tesseract

`sudo apt install tesseract-ocr`

这里是ubuntu安装示例，如果是其它服务器，参考官方的文档

官方安装地址：`https://tesseract-ocr.github.io/tessdoc/Installation.html`

ubuntu 安装软件后的路径一般都是`/usr/share`,如果不清楚的可以命令查找

`whereis tesseract-ocr`

这样可以得到安装路径，安装语言包的时候需要用到。

3.安装语言包

打开github仓库：https://github.com/tesseract-ocr/tessdata

`chi_sim.traineddata`就是中文语言包，下载之后，放到tesseract的安装路径下的`tessdata`目录下。

4.运行`py test.py`代码，应该就能看到识别内容了。


## 注意问题

识别不是百分百的准确，如果想要正确的识别图片，你需要对图片进行预处理，字符过滤，甚至是模型训练等方法。

图片预处理，例如二值化、去噪、倾斜校正等。这些预处理步骤可以提高图像的质量，从而减少识别错误和不能识别的部分。

下面提供一个简单案例，把彩色图片转成黑白，然后在进行识别。
```
# coding: utf-8
import pytesseract
from PIL import Image

def filter_and_recognize_image(image_path):
    # 读取图像
    image = Image.open(image_path)
    # 灰度处理
    image = image.convert('L')
    # 设置二值化的阈值
    threshold = 170
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 通过表格转换成二进制图片，1的作用是白色，0就是黑色
    image = image.point(table, "1")
    # 进行文本识别
    text = pytesseract.image_to_string(image,lang='chi_sim')
    # 删除冗余字符
    text = text[0:-1]
    return text

# 示例用法
image_path = "test.png"
filtered_text = filter_and_recognize_image(image_path)
print(filtered_text)
```

只是简单示例，更多使用方法请参考官方文档！

官方文档地址：`https://tesseract-ocr.github.io/tessdoc/`