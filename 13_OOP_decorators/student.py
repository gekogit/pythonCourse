import datetime
from holidays import Poland


class Student:
    university = 'university'
    min_avg = 4.7

    def __init__(self, name, last, grades):
        self.name = name
        self.last = last
        self.grades = grades
        self.nick_name = name +'***'

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    @classmethod
    def set_univer_name(cls, new_name):
        cls.university = new_name

    def email(self):
        return f'{self.last}.{self.name}@{self.university}.com'

    def grand_scholarship(self):
        if self.grades > self.min_avg:
            print("You get scholarship")
        else:
            print("Not this time")

    @classmethod
    def set_new_avg(cls, new_value):
        cls.min_avg = new_value

    @staticmethod
    def academic_day(day):
        pl_holidays = Poland()
        print(pl_holidays)
        if day.weekday() == 5 or day.weekday() == 6 or day not in pl_holidays:
            return 'Nie'
        else:
            return 'Tak'


obj_anna = Student('anna', 'kowalska', 4.72)
obj_michal = Student('michal', 'nowak', 4.69)

obj_michal.grand_scholarship()

obj_michal.set_new_avg(4.5)
obj_michal.grand_scholarship()

print(obj_anna.min_avg)
print(obj_michal.min_avg)
print('****')
Student.set_new_avg(4.1)
print(obj_anna.min_avg)
print(obj_michal.min_avg)


print('----------------')
print(obj_michal.email())
print(obj_anna.email())
Student.set_univer_name("hell_place")
print('changed name')
print(obj_michal.email())
print(obj_anna.email())
today = datetime.date.today()
print(today)
print('Czy dzisiaj są zajęcia? ', Student.academic_day(today))

