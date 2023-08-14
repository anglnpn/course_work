import json
import datetime
from operator import itemgetter
from classes import Operation


def unpacking_json(file_name="operations.json"):
    """
    Функция распаковывает json.
    Сортирует элементы списка по успешности операции "EXECUTED"
    и добавляет их в список. Список сортерует и получает новый список с
    последними 5 операциями"
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

    executed_list_3 = sorted(executed_list_2, key=itemgetter("date"))
    last_5_operation = executed_list_3[-5:]

    total_list = []

    for oper in last_5_operation:
        try:
            date = oper["date"]
            amount = oper["operationAmount"]["amount"]
            currency = oper["operationAmount"]["currency"]["name"]
            description = oper["description"]
            to_ = oper["to"]
            from_ = oper["from"]

        except KeyError:
            from_ = False

        operations_s = Operation(date, amount, currency, description, to_, from_)
        total_list.append(operations_s)

    return total_list


def get_from_check_or_card(operation):
    """
    Получет объект from.
    Определяет счет это или карта.
    Шифрует в зависимости от типа.
    """
    _from = operation.get_from_()
    if operation.get_from_():
        for i in _from.split():
            if i == 'Счет':
                check_from = _from.split()[0] + ' **' + _from.split()[1][-4:]
                return check_from
            else:
                if i == 'Visa':
                    card_from = f"{i} {_from.split()[1]} {_from[-16:-12]} {_from[-12:-10]}** **** {_from[-4:]}"
                    return card_from
                else:
                    card_from = f"{i} {_from[-16:-12]} {_from[-12:-10]}** **** {_from[-4:]}"
                    return card_from
    else:
        return False


def get_to_check_or_card(operation):
    """
    Получет объект to.
    Определяет счет это или карта.
    Шифрует в зависимости от типа.
    """
    _to = operation.get_to_()
    for i in _to.split():
        if i == 'Счет':
            check_from = _to.split()[0] + ' **' + _to.split()[1][-4:]
            return check_from
        else:
            if i == 'Visa':
                card_from = f"{i} {_to.split()[1]} {_to[-16:-12]} {_to[-12:-10]}** **** {_to[-4:]}"
                return card_from
            else:
                card_from = f"{i} {_to[-16:-12]} {_to[-12:-10]}** **** {_to[-4:]}"
                return card_from


def get_from_and_to(operation):
    """
    Вызывает функции с объектами.
    Определяет как вывод информацию пользователю.
    """
    from_ = get_from_check_or_card(operation)
    to_ = get_to_check_or_card(operation)
    if from_:
        return f'{from_} -> {to_}'
    else:
        return to_


def formate_date(operation):
    """
    Получает дату.
    Конвертирует ее в нормальный вид.
    """
    str_data = str(operation.get_date())
    str_data = str_data[:8]
    date = datetime.datetime.strptime(str_data, '%Y%m%d')
    return date.strftime('%d.%m.%Y')
