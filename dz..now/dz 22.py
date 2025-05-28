# class KgPounds:
#     def __init__(self, x=12):
#         self.__x = x
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return f"{self.__x}, Кг => {round(self.__x * 2.205, 2)} фунтов"
#
#     @x.setter
#     def x(self, x):
#         if KgPounds.__check_value(x):
#             self.__x = x
#         else:
#             print("Килограммы задаются только числами")
#
#
# p1 = KgPounds()
# print(p1.x)
# p1.x = 41
# print(p1.x)
# p1.x = "abc"
