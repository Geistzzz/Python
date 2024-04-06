class Student:
    student_id = 8


def main():
    print(Student.__name__)

    print(Student.student_id)

    print(getattr(Student, "student_id"))

    print(getattr(Student, "unknown", None))

    Student.student_id = 80

    setattr(Student, "student_id", 800)

    print(getattr(Student, "student_id"))
    # 反射机制

    Student.new = "new student"

    del Student.new

    Student.new = "new student"

    delattr(Student, "new")

    s1 = Student()

    s2 = Student()

    Student.student_id = 4

    print(s1.student_id)
    print(s2.student_id)

    from pprint import pprint
    pprint(Student.__dict__)


if __name__ == '__main__':
    main()
