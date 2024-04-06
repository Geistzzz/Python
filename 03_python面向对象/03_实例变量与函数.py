class Student:
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello World!")


def main():
    s1 = Student('zc')
    s1.sayHello()


if __name__ == '__main__':
    main()
