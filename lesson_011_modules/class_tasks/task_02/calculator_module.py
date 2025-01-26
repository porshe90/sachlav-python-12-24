def _add(x, y):
    return x + y


def _subtract(x, y):
    return x - y


def _multiply(x, y):
    return x * y


def _divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return x / y


def calculate(x, y, operation):

    match operation:
        case '+':
            return _add(x, y)
        case '-':
            return _subtract(x, y)
        case '*':
            return _multiply(x, y)
        case '/':
            return _divide(x, y)
        case _:
            raise ValueError(f"Неверная операция: {operation}")