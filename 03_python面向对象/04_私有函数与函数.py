class Student:
    def __init__(self, name):
        self.__name = name

    def __say_hello(self):
        print("Hello World!", self.__name)


def main():
    s1 = Student('zc')
    s1._Student__say_hello()
    # print(s1.__name)
    print(s1._Student__name)
    # 方法同

if __name__ == '__main__':
    main()
