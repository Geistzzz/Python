import yaml

# 读取 YAML 文件 (utf-8是解码方式吧)
with open("G:\Python\data\example.yaml", "r", encoding='utf-8') as file:
    # print(type(file))
    data = yaml.safe_load(file)['subject'].split(",")  # 会变成一个字典

    # data = yaml.load(file, yaml.FullLoader)['subject'].split(",")  # 会变成一个字典

# print(type(data))
print(data)
# 写入 YAML 文件
# with open("G:\Python\data\example.yaml", "w") as file:
#     yaml.safe_dump(data, file, default_flow_style=False)
