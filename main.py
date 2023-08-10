from classes import Operations
from utils import unpacking_json, get_from_and_to


unpacking_json = unpacking_json()

user_input = input('Для вывода информации о последних 5 операциях нажмите Enter\n')
for operation in unpacking_json:
    print(f'{operation.get_data()} {operation.get_description()}\n'
          f'{get_from_and_to(operation)}\n'
          f'{operation.get_amount()}\n')








