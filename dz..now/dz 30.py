import json


class CountryCapital:
    @staticmethod
    def add_country(file_name):
        new_country = input("Введите название страны: ").lower()
        new_capital = input("Введите название столицы: ").lower()

        try:
            data = json.load(open(file_name, encoding="utf-8"))
        except FileNotFoundError:
            data = {}

        data[new_country] = new_capital

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, encoding="utf-8") as f:
            print({k.title(): v.title() for k, v in json.load(f).items()})

    @staticmethod
    def delete_country(file_name):
        del_country = input("Введите название страны: ").lower()

        try:
            data = json.load(open(file_name, encoding="utf-8"))
        except FileNotFoundError:
            data = {}

        if del_country in data:
            del data[del_country]

            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    def search_data(file_name):
        country = input("Введите название страны: ").lower()

        try:
            data = json.load(open(file_name, encoding="utf-8"))
        except FileNotFoundError:
            data = {}

        if country in data:
            print(f"Страны {country.title()} столица {data[country].title()} есть в словаре")
        else:
            print(f"Страны {country.title()} нет в словаре")

    @staticmethod
    def edit_data(file_name):
        country = input("Введите страну для корректировки: ").lower()
        new_capital = input("Введите новое название столицы: ").lower()

        try:
            data = json.load(open(file_name, encoding="utf-8"))
        except FileNotFoundError:
            data = {}

        if country in data:
            data[country] = new_capital

            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет")


file = "list_capital.json"
while True:
    index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                  "4 - редактирование данных\n5 - просмотр данных\n6 -завершение работы\n"
                  "Ввод: ")
    if index == "1":
        CountryCapital.add_country(file)
    elif index == "2":
        CountryCapital.delete_country(file)
    elif index == "3":
        CountryCapital.search_data(file)
    elif index == "4":
        CountryCapital.edit_data(file)
    elif index == "5":
        CountryCapital.load_from_file(file)
    elif index == "6":
        break
    else:
        print("Введен некорректный номер")

    print("*" * 50)


