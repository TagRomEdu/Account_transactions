from settings import OPERATIONS_PATH
from app.utils import get_operations, get_executed_ops, sort_list_of_5, output_info


def main():
    print(output_info(sort_list_of_5(get_executed_ops(get_operations(OPERATIONS_PATH)))))


if __name__ == "__main__":
    main()
