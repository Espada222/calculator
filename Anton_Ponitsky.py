def calculator():
    running = True

    while running:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))

            operation = input("Выберите операцию (+, -, *, /) или 'exit' для выхода: ")

            if operation == '+':
                result = a + b
            elif operation == '-':
                result = a - b
            elif operation == '*':
                result = a * b
            elif operation == '/':
                result = a / b
            elif operation == 'exit':
                running = False
                continue
            else:
                print("Некорректная операция. Попробуйте снова.")
                continue

            print(f"Результат: {result}")

        except ZeroDivisionError:
            print("Деление на ноль запрещено.")
        except ValueError:
            print("Ошибка: Пожалуйста, вводите только числа.")

    print("Калькулятор завершен.")

calculator()

calculator()
