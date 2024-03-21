import codecs

"""
字符编码方式有很多种，常见的有：Unicode、ASCII、GBK、GB2312、UTF-8。
其中，Unicode 是一种国际标准，用于给全球各种语言的字符分配唯一的数字标识符；
ASCII 是美国在19世纪60年代为了建立英文字符和二进制的关系时制定的编码规范，
它能表示128个字符；GBK 和 GB2312是中国的汉字编码标准；
UTF-8是 Unicode 标准的一种实现方式，用于在网页、电子邮件等场景中传输和存储文本数据。
"""

# 编码文本
encoded_text = codecs.encode("你好，世界！", "gbk")
print(encoded_text)

# 解码文本
decoded_text = codecs.decode(encoded_text, "utf-8")
print(decoded_text)
