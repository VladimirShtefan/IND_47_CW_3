import json
from pathlib import Path

from src.operations import Operation


def load_operations(path: Path) -> list[dict]:
    """

    :param path:
    :return:
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def load_operations_instances(operations: list[dict]) -> list[Operation]:
    """

    :param operations:
    :return:
    """
    return [
        Operation(
            date=operation["date"],
            state=operation["state"],
            amount=operation["operationAmount"]["amount"],
            currency_name=operation["operationAmount"]["currency"]["name"],
            description=operation["description"],
            from_=operation.get("from", ""),
            to=operation["to"]
        )
        for operation in operations
        if operation
    ]


def get_executed_operations(operations: list[Operation]) -> list[Operation]:
    """
    Докстринга
    :param operations:
    :return:
    """
    return [
        operation
        for operation in operations
        if operation.state == "EXECUTED"
    ]


def sort_operations_by_date(operations: list[Operation]) -> list[Operation]:
    """

    :param operations:
    :return:
    """
    return sorted(operations, reverse=True)
