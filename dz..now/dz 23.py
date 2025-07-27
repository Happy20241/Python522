class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self._num = num
        self._surname = surname
        self._percent = percent
        self._value = value
        print(f"Счёт #{self._num} принадлежащий {self._surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счёт #{self._num}  принадлежащий {self._surname} был закрыт.")

    # --- Class & Static Methods ---
    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    # --- Properties: surname ---
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, name):
        self._surname = name

    # --- Properties: value ---
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if val >= 0:
            self._value = val
        else:
            print("Ошибка: Баланс не может быть отрицательным.")

    # --- Alternative get/set methods ---
    def get_surname(self):
        return self._surname

    def set_surname(self, name):
        self._surname = name

    def get_value(self):
        return self._value

    def set_value(self, val):
        if val >= 0:
            self._value = val
        else:
            print("Ошибка: Баланс не может быть отрицательным.")

    # --- Account operations ---
    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счёта: {usd_val} {Account.suffix_usd}")

    def convert_tu_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счёта: {eur_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счёте:")
        print("-" * 20)
        print(f"#{self._num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self._percent:.0%}")
        print("-" * 20)

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self._percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withraw_maney(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()