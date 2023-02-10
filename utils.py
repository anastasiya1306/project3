from datetime import datetime

def get_filtered_operation(result_data):
    """
    Возвращает отсортированный список выполненных (EXECUTED) клиентом операций
    """
    operation_executed = []
    for index in result_data:
        if 'state' in index and index['state'] == "EXECUTED":
            operation_executed.append(index)
    return operation_executed


def get_from_operation(result_data):
    """
    Возвращает отсортированный список, содержащий информацию об отправителе
    """
    from_operation = []
    for index in result_data:
        if 'from' not in index:
            continue
        else:
            from_operation.append(index)
    return from_operation


def get_last_five_operation(operation_executed):
    """
    Возвращает список пяти последних операций
    """
    operation_executed = sorted(operation_executed, key=lambda x: x["date"], reverse=True)
    last_five_operation = operation_executed[:5]
    return last_five_operation


def get_date(operation_date):
    """
    Возвращает дату в нужном формате
    """
    date = datetime.strptime(operation_date['date'], "%Y-%m-%dT%H:%M:%S.%f")
    date = datetime.strftime(date, "%d.%m.%Y")
    return date


def get_description(last_five_operation):
    return last_five_operation['description']


def get_from(last_five_operation):
    sender = last_five_operation['from'].split()
    from_digits = sender.pop()
    from_ = " ".join(sender)
    from_all = f"{from_} {from_digits[:4]} {from_digits[4:6]}** **** {from_digits[-4:]}"
    return from_all


def get_to(last_five_operation):
    receiver = last_five_operation['to'].split()
    to_digits = receiver.pop()
    to_bill = " ".join(receiver)
    to_all = f'{to_bill} **{to_digits[-4:]}'
    return to_all


def get_operation_amount(operation):
    return f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"