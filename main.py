from classes import Operations
from utils import unpacking_json


unpacking_json = unpacking_json()

user_input = input('Для вывода информации о последних 5 операциях нажмите Enter')
for a in unpacking_json:
    print(f'{a.get_data()} {a.get_description()}\n'
          f'{a.get_from_to()}\n'
          f'{a.get_amount()}\n')





