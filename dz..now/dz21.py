class Car:
    def __init__(self):
        self.model_name = "Х7 М501"
        self.year_of_release = 2021
        self.manufacturer = "BMW"
        self.engine_power = 530
        self.color = "white"
        self.price = 10790000

    def input_data(self):
        self.model_name = input("Введите название модели: ")
        self.year_of_release = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_power = int(input("Введите мощность двигателя (л.с.): "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print("Данные автомобиля".center(40, "x"))
        print(f"Название модели: {self.model_name}")
        print(f"Год выпуска: {self.year_of_release}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Мощность двигателя: {self.engine_power} л.с.")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
        print("=" * 40)

    def get_model_name(self):
        return self.model_name

    def set_model_name(self, name):
        self.model_name = name

    def get_year_of_release(self):
        return self.year_of_release

    def set_year_of_release(self, year):
        self.year_of_release = year

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_engine_power(self):
        return self.engine_power

    def set_engine_power(self, power):
        self.engine_power = power

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


car = Car()
car.display_data()

car.set_price(11000000)
print("Обновленная цена:", car.get_price())