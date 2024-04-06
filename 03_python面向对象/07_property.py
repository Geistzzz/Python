class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 200:
            raise ValueError("error")
        self.__age = age

    def __str__(self):
        return f'{self.__name, self.__age}'


def main():
    s = Student('zhang_san', 18)
    s.age = 3
    print(s)


if __name__ == '__main__':
    main()
