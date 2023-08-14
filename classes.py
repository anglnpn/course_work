"""
Импорт декоратора и функции для автоматического
добавления сгенерированных специальных методов
"""
from dataclasses import dataclass


@dataclass
class Operation:
    """
    Класс принимающий значения
    о операциях пользователя
    """
    date: str = ''
    amount: str = ''
    currency: str = ''
    description: str = ''
    to_: str = ''
    from_: str = ''

    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def get_from_(self):
        return self.from_

    def get_to_(self):
        return self.to_

    def get_amount(self):
        return f'{self.amount} {self.currency}'

    def __str__(self):
        """
        Возвращает информацию
        для вывода пользователю
        """
        from utils import get_from_and_to
        from utils import formate_date
        return (f'{formate_date(self)} {self.get_description()}\n'
                f'{get_from_and_to(self)}\n'
                f'{self.get_amount()}\n')
