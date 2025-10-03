"""как создаются функции"""
from урок6 import surname


# определение наименование(параметры):
#       тело функции (логика функции)
#       возврашение обьекта(результат)

# наименование(АРГУМЕНТЫ)

# def funk_name():
#     print(f'name: {name} surname: {surname}')

# funk_name()


# def gat_birth_year(name: str, age: int) -> str:

def func_name(name: str, age: int) -> str:
    """Все работает"""
    name = name.title()
    age = 2025 - age
    return f'name:{name} b_year:{age}'

text = input('text your name and age')
print(func_name('Avi', 19))
