class Wallet:

    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        elif sum([True for i in currency if i.islower()]):
            raise ValueError("Название должно состоять только из заглавных букв")
        else:
            self.balance = balance
            self.currency = currency

    def __eq__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return other.balance == self.balance
        elif not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        else:
            raise ValueError("Нельзя сравнить разные валюты")

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(self.currency, self.balance - other.balance)
