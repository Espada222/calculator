def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def test_max_number():
    assert max_number(10, 9) == 10
    assert max_number(5, 10) == 10
    assert max_number(5, 5) == 5
    assert max_number(0, 10) == 10
    assert max_number(0, -10) == 0
    assert max_number(-1, -10) == -1
    print("Тесты пройдены")


test_max_number()

result1 = max_number(2, 1)

result2 = max_number(1, 3)
print(result1)
print(result2)


def empty_function():
    pass


empty_function()


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


n = 25
for num in even_numbers(n):
    print(num)
