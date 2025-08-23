# class Time:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         total_seconds = hours * 3600 + minutes * 60 + seconds
#         self.total_seconds = total_seconds
#
#     @classmethod
#     def from_string(cls, time_str):
#         h, m, s = map(int, time_str.split(':'))
#         return cls(h, m, s)
#
#     def __str__(self):
#         h = self.total_seconds // 3600
#         m = (self.total_seconds % 3600) // 60
#         s = self.total_seconds % 60
#         return f"{h:02d}:{m:02d}:{s:02d}"
#
#     def __add__(self, other):
#         if isinstance(other, Time):
#             return Time(seconds=self.total_seconds + other.total_seconds)
#         return NotImplemented
#
#     def __sub__(self, other):
#         if isinstance(other, Time):
#             diff = abs(self.total_seconds - other.total_seconds)
#             return Time(seconds=diff)
#         return NotImplemented
#
#     def __floordiv__(self, other):
#         if isinstance(other, Time):
#             if other.total_seconds == 0:
#                 raise ZeroDivisionError("Деление на нулевое время")
#             quotient = self.total_seconds // other.total_seconds
#             return Time(seconds=quotient)
#         return NotImplemented
#
#     def __mod__(self, other):
#         if isinstance(other, Time):
#             if other.total_seconds == 0:
#                 return Time(0, 0, 0)
#             remainder = self.total_seconds % other.total_seconds
#             return Time(seconds=remainder)
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, Time):
#             self.total_seconds += other.total_seconds
#             return self
#         return NotImplemented
#
#     def __isub__(self, other):
#         if isinstance(other, Time):
#             self.total_seconds -= other.total_seconds
#             if self.total_seconds < 0:
#                 self.total_seconds = 0
#             return self
#         return NotImplemented
#
#     def __ifloordiv__(self, other):
#         result = self.__floordiv__(other)
#         self.total_seconds = result.total_seconds
#         return self
#
#     def __imod__(self, other):
#         result = self.__mod__(other)
#         self.total_seconds = result.total_seconds
#         return self
#
#
# c1 = Time.from_string("00:10:00")
# c2 = Time.from_string("00:06:40")
#
# print(f"c1: {c1}")
# print(f"c1 + c2: {c1 + c2}")
# print(f"c1 - c2: {c1 - c2}")
#
# # Деление и остаток:
# print(f"c1 // c2: {c1 // c2}")
# print(f"c1 % c2: {c1 % c2}")
#
# c1 = c2
# print(f"После присваивания c1=c2: {c1}")
#
# c3 = Time.from_string("22:13:20")
# c1 = c3
# print(f"После присваивания c1=c3: {c1}")
#
# c1 //= c2
# print(f"После //= c2 : {c1}")
#
# c1 %= c2
# print(f"После %= c2 : {c1}")