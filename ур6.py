"""как создаются функции"""



# определение наименование(параметры):
#       тело функции (логика функции)
#       возврашение обьекта(результат)

# наименование(АРГУМЕНТЫ)

# def funk_name():
#     print(f'name: {name} surname: {surname}')

# funk_name()


# def gat_birth_year(name: str, age: int) -> str:

"""вариант 1 это я сама сделала"""

# def func_name(name: str, age: int) -> str:
#     """Все работает"""
#     name = name.title()
#     age = 2025 - age
#     return f'name:{name} b_year:{age}'

# text = input('text your name and age')
# print(func_name('Avi', 19))

# """вариант 2 """

# def get_birth_year(name: str, age: int) -> str:
#     """Функция принимает имя и возраст, возвращает Имя и год рождения"""
#     current_year = 2025
#     birth_year = current_year - age
#     return f'{name.title()}, год рождения: {birth_year}'


# print(get_birth_year('azamat', 20))


# реализация функции
square_2 = get_square(width:7,)