import json
import request
import datetime


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

    for executed_operation in executed_list:
        date = datetime.datetime.strptime(executed_operation.get("date"), '%Y-%m-%dT%H:%M:%S.%f')
        new_date = f'{date:%Y%m%d%H%M%S%f}'
        executed_operation["date"] = new_date
        print(new_date)
        print(executed_operation)


print(unpacking_json())
