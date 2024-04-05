class Human:
    @staticmethod
    def __new__(cls, *args, **kwargs):
        class_ = super(Human, cls).__new__(cls)
        # class_.freedom = True
        if kwargs:
            for name, value in kwargs.items():
                setattr(class_, name, value)
        return class_


class Student(metaclass=Human, country="China"):
    pass


print(Student.country)
