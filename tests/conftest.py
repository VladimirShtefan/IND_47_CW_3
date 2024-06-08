import pytest

from src.operations import Operation


@pytest.fixture
def operations_json():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                }
            },
            "description": "Перевод организации",
            "to": "Счет 64686473678894779589"
        },
        {},
        {
            "state": "asdasdsad",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "MasterCard 7158300734726758"
        },
        {
            "state": "EXECUTED",
            "date": "2015-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "state": "asdasdasdsadsa",
            "date": "2022-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },

    ]


@pytest.fixture
def operations_instance():
    return Operation(
        date="2019-08-26T10:50:58.294041",
        state="EXECUTED",
        amount="9824.07",
        currency_name="USD",
        description="Перевод организации",
        from_="Счет 75106830613657916952",
        to="MasterCard 7158300734726758"
    )
