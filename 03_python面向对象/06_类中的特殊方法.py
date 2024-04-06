class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        print("str is called")
        return f"{self.year}-{self.month}-{self.day}"

    def __eq__(self, other):
        print("eq is called")
        if not isinstance(other, MyDate):
            return False
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __hash__(self):
        print("hash is called")
        return hash((self.year + self.month * 101, self.day * 101))

    def __bool__(self):
        print("bool is called")
        return self.year > 2021


def main1():
    my_date1 = MyDate(2022, 11, 3)
    my_date2 = MyDate(2022, 11, 3)
    my_date3 = MyDate(2020, 11, 3)

    print(str(my_date1))
    print(my_date1)  # 其实是打印里面的__str__方法

    print(my_date1 is my_date2)
    print(my_date1 == my_date2)

    date_set = set()
    date_set.add(my_date1)

    print(bool(my_date3))


if __name__ == "__main__":
    main1()
