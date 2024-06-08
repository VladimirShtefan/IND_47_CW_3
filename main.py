from settings import OPERATIONS_PATH, COUNT_OPERATIONS
from src.utils import (
    load_operations,
    load_operations_instances,
    get_executed_operations,
    sort_operations_by_date
)


def main():
    operations1 = load_operations(OPERATIONS_PATH)
    operations_instances = load_operations_instances(operations1)
    ex_op = get_executed_operations(operations_instances)
    sort_op = sort_operations_by_date(ex_op)[:COUNT_OPERATIONS]
    for op in sort_op:
        print(op)


if __name__ == '__main__':
    main()
