print("Выберите операцию:")

while True:
    choice = input("Введите какую операцию хотите выполнить (+/-/*//): ")

    if choice in ['+', '-', '*', '/']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Ошибка! Деление на ноль.")

        next_calculation = input("Хотите выполнить еще один расчет? (да/нет): ")
        if next_calculation.lower() != 'да':
            break
    else:
        print("Некорректный ввод. Пожалуйста, выберите операцию снова.")
try:
    result = num1 / num2
except ZeroDivisionError:
    result = "Деление на ноль запрещено"
    input()
