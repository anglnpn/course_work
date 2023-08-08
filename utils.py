import json
import request
import datetime
from operator import itemgetter
from classes import Operations

def unpacking_json():
    """
    Функция распаковывает json.
    Сортирует элементы списка по успешности операции
    и добавляет их в список"
    """
    file = open("operations.json", encoding='utf-8')
    list_json = json.load(file)
    executed_list = []
    for operation in list_json:
        if operation.get("state") == "EXECUTED":
            executed_list.append(operation)
        else:
            continue

    """
     Получаем дату операции. Именяем ее формат.
     Меняем значение в словаре по ключу.
     """

    executed_list_2 = []

    for executed_operation in executed_list:
        date = datetime.datetime.strptime(executed_operation.get("date"), '%Y-%m-%dT%H:%M:%S.%f')
        new_date = f'{date:%Y%m%d%H%M%S%f}'
        executed_operation["date"] = int(new_date)
        executed_list_2.append(executed_operation)
        # print(new_date)
        # print(executed_operation)

    executed_list_3 = sorted(executed_list_2, key=itemgetter("date"))

    last_5_operation = executed_list_3[-5:]
    for i in last_5_operation:

    operations = Operations()

unpacking_json()
