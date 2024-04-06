class Student:
    pass


# isinstance()函数 怎么判断某个对象是不是某个类型
def main():
    print(type(Student))
    print(isinstance(Student, type))
    print(Student)
    student = Student()
    print(student)
    print(hex(id(student)))
    print(isinstance(student, Student))


if __name__ == '__main__':
    main()
