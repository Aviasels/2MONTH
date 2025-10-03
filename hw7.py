def nearest_number(numbers, target):
    sorted_list = sorted(numbers, key=lambda x: abs(x - target))
    return (target, sorted_list)
input_str = input("Введите числа через пробел: ")

numbers = list(map(int, input_str.split()))

target = int(input("Введите целевое число: "))

result = nearest_number(numbers, target)
print("Результат:", result)

lambda + map
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Квадраты чисел:", squares)
"""
lambda + filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Чётные числа:", even_numbers) 

def element_by_index(iterable=[1, 2, 3, 4, 5]):
    length = len(iterable)
    print(f"Индексы доступны от 0 до {length - 1}")
    print("Чтобы выйти, введите 'exit'")
    while True:
        s = input("Введите индекс: ")
        if s.lower() == 'exit':
            print("Выход из программы.")
            break
        if not s.isdigit():
            print("Пожалуйста, введите число или 'exit' для выхода.")
            continue
        index = int(s)
        if 0 <= index < length:
            print(f"Элемент: {iterable[index]}")
        else:
            print(f"Ошибка: индекс должен быть от 0 до {length - 1}")
    element_by_index()
