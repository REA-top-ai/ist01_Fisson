class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_role_info(self):
        return f'Персона с именем {self.__name}'


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__grades = []

    def add_grades(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            return "Ошибка: баллы студентов должны быть в диапозоне от 0 до 100"

    def avg_grade(self):
        return sum(self.__grade) / len(self.__grades)

    def get_role_info(self):
        return f'Студент{self.__name}, ID:{self.__student_id}, Средний балл:{self.avg_grade()}'


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject
        self.__salary = 0

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            return "Ошибка: зарплата должна быть больше 0."

    def get_salary(self):
        return self.__salary

    def get_role_info(self):
        return f'Преподаватель {self.__name} ведет дисциплину {self.__subject}'


p1 = Person('Иван', 23)
print(p1.get_role_info())

s1 = Student('IST01')
print(s1)