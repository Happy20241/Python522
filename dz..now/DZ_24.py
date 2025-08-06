# from math import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def edit_a(self, a):
#         self.a = a
#
#     def edit_b(self, b):
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#     def mult(self):
#         return self.a * self.b
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.c = self.hypotenuse()
#
#     def hypotenuse(self):
#         hypot = round(sqrt(self.a ** 2 + self.b ** 2), 2)
#         print(f"Гипотенуза ABC: {hypot}")
#         return hypot
#
#     def print_info(self):
#         print(f"Прямоугольный треугольник ABC: ({self.a}, {self.b}, {self.c})")
#
#     def square(self):
#         s = 0.5 * self.mult()
#         print(f"Площадь ABC: {s}")
#
#     def edit_a(self, a):
#         super().edit_a(a)
#         self.c = self.hypotenuse()
#
#     def edit_b(self, b):
#         super().edit_b(b)
#         self.c = self.hypotenuse()
#
#
# tr = RightTriangle(5, 8)
# tr.print_info()
# tr.square()
# print()
#
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
#
# print()
#
# tr.edit_a(10)
# tr.edit_b(20)
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# tr.square()