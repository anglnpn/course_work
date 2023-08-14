"""
Импорт функции
"""
from utils import unpacking_json

unpacking_json = unpacking_json()

"""
Вывод информации пользователю о последних 5 операций
"""
user_input = input(f'Для вывода информации о последних {len(unpacking_json)} операциях нажмите Enter\n')
for operation in unpacking_json:
    print(operation)

