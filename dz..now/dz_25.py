# from abc import ABC, abstractmethod
#
#
# class Human(ABC):
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @abstractmethod
#     def print_info(self):
#         pass
#
#     def person_info(self):
#         return f"{self.surname}, {self.name}, {self.age}, {self.print_info()}"
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, study, group, average):
#         super().__init__(surname, name, age)
#         self.study = study
#         self.group = group
#         self.average = average
#         print(self.person_info())
#
#     def print_info(self):
#         return f"Study: {self.study}, Group: {self.group}, Avg: {self.average}"
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, discipline, skill):
#        super().__init__(surname, name, age)
#        self.discipline = discipline
#        self.skill = skill
#        print(self.person_info())
#
#     def print_info(self):
#         return f"Discipline: {self.discipline}, Skill: {self.skill}"
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, study, group, average, project):
#        self.project = project
#        super().__init__(surname, name, age, study, group, average)
#        print(self.person_info())
#
#     def print_info(self):
#         return f"{super().print_info()}, Project: {self.project}"
#
#
# st1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5)
# st2 = Student("Загидуллин", "Линар", 32, "РПО", "Pd_011", 5)
# gr1 = Graduate("Шугани", "Сергей", 15, "РПО", "Pd_011", 5, "Защита персональных данных")
# tch1 = Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110)
# st3 = Student("Маркин", "Данил", 16, "ГК", "Python_011", 5)
# tch2 = Teacher("Башкиррв", "Алексей", 43, "Разработка приложений", 20)
