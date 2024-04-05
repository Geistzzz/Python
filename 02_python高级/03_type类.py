class Student(object):
    def greeting(self):
        print("Hello ")


print(type(Student))
print(isinstance(Student, type))

class_body = """
def greeting(self):
    print("Hello")
"""
class_dict = {}
exec(class_body, globals(), class_dict)
Customer = type("Customer", (object,), class_dict)
c = Customer()
c.greeting()

# 软件先写，功能后写，后写的东西使用文本文件提供的
