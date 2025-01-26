from calculator_module import calculate


def main():
    print("Добро пожаловать в калькулятор!")
    try:
        # Запрос входных данных от пользователя
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")

        # Вызов функции calculate и вывод результата
        result = calculate(x, y, operation)
        print(f"Результат: {result}")

    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except ZeroDivisionError as zde:
        print(f"Ошибка: {zde}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()