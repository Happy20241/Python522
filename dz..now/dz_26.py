# class Student:
#     def __init__(self, name, laptop_model, laptop_processor, laptop_memory):
#         self.name = name
#         self.laptop = self.Laptop(laptop_model, laptop_processor, laptop_memory)
#
#     def print_info(self):
#         print(f"Студент: {self.name}")
#         self.laptop.print_info()
#
#     class Laptop:
#         def __init__(self, model, processor, memory):
#             self.model = model
#             self.processor = processor
#             self.memory = memory
#
#         def print_info(self):
#             print(f"Ноутбук: Модель - {self.model}, Процессор - {self.processor}, Память - {self.memory} ГБ")
#
#
# student1 = Student("Roman", "НР", "17", 16)
# student2 = Student("Vladimir", "HP", "i7", 16)
#
#
# student1.print_info()
# print()
# student2.print_info()