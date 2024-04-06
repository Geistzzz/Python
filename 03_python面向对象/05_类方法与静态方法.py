class Student:
    school = 'abc'
    @classmethod
    def hello(cls):
        print("Hello World!")

    @staticmethod
    def out():
        print(f"Hello {Student.school}")
        

def main():
    Student.hello()
    Student.out()


if __name__ == '__main__':
    main()
