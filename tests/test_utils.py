from utils import*

def test_get_filtered_operation(test_filtered_operation):
    assert len(get_filtered_operation(test_filtered_operation)) == 4


def test_get_from_operation(test_filtered_operation):
    assert len(get_from_operation(test_filtered_operation)) == 2


def test_get_last_five_operation(test_filtered_operation):
    data = get_last_five_operation(test_filtered_operation)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'


def test_get_date(test_filtered_operation):
    data = get_date(test_filtered_operation[0])
    assert data == '26.08.2019'


def test_get_description(test_filtered_operation):
    data = get_description(test_filtered_operation[0])
    assert data == 'Перевод организации'


def test_get_from(test_filtered_operation):
    data = get_from(test_filtered_operation[2])
    assert data == 'MasterCard 7158 30** **** 6758'


def test_get_to(test_filtered_operation):
    data = get_to(test_filtered_operation[1])
    assert data == 'Счет **5560'


def test_get_operation_amount(test_filtered_operation):
    data = get_operation_amount(test_filtered_operation[4])
    assert data == '79114.93 USD'