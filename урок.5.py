# # Словари- dict множества-set.
# # {key: value} {ключ: значение}
#
# # cities_list = ['tokmok', 'kant', 'bishkek', 'karakol']
# # cities_dict = {
# #     'tokmok': 80000,
# #     'kant': 85000,
# #     'bishkek': 1_000_000,
# #     'karakol': 78000
# # }
#
# # beshbarmak = {"лапша", "мясо", "лук"}
# # plov = {"рис",  "марковь", "мясо"}
# #
# # print(beshbarmak.issubset(plov))
# # print(beshbarmak.issubset(["лапша", "рис", "гречка", "лук", "томат", "курица"]))
# # print(beshbarmak.union(plov))
# # print(beshbarmak.difference(plov))
# # print(beshbarmak.intersection(plov))
# # print(beshbarmak.symmetric_difference(plov))
#
# # numbers1 = [1, 2, 3, 2, 4, 1, 3]
# # numbers2 = {1, 2, 3, 2, 4, 1, 3}
#
# # print(numbers1)
# # print(numbers2)
# # print(type(numbers2))
#
# # student = {
# #     'name': 'aruuke',
# #     'age': 19,
# #     'surname': 'popova',
# #     'country': 'RUS',
# #     'hobby': ['chess', 'books']
# # }
#
# # print(student.items())
# # for key, value in student.items():
# #     print(f'{key} : {value}')
#
# # print(student.keys())
# # print(student.values())
#
#
# # print(student)
#
# """удаление"""
# # student.pop('name')
# # del student['age']
#
# """изменение"""
# # student['name'] = 'Aruuke'
# # student['age'] += 1
#
# """добавление"""
# # student['height'] = 1.64
# # student.update({'country': 'KGZ', 'surname': 'petrova'})
#
# # print(student)
#
# """Доступ к значениям словаря всегда через ключ"""
# # print(student['name'])
# # print(student['age'])
#
# # print(type(student))
#
#
#
# # print("Программа приветствия со светофором!")
# # print("Введите цвет светофора (зеленый, желтый, красный) или 'выход' для завершения.")
#
# # while True:
# #     цвет = input("Введите цвет: ").lower()  # приводим к нижнему регистру
#
#     # if цвет == "выход":
#     #     print("Программа завершена. До свидания!")
#     #     break
#     # elif цвет == "зеленый":
#     #     print("Можно идти.")
#     # elif цвет == "желтый":
#     #     print("Подожди немного.")
#     # elif цвет == "красный":
#     #     print("Стой!")
#     # else:
#     #     print("Неверный ввод. Пожалуйста, введите: зеленый, желтый, красный или выход.")
# # расходы = [ ]
#
# # for день in range(1, 8):
# #     расход = float(input(f"Введите расход за день {день}: "))
# #     расходы.append(расход)
#
# # общий_расход = sum(расходы)
# # print(f"\nОбщий расход за 7 дней: {общий_расход} сом")
#
#
#
# print("Программа приветствия со светофором!")
# print("(зеленый, желтый, красный) или 'выход' для завершения.")
#
# while True:
#     цвет = input("Введите цвет: ").lower()
#
#     if цвет == "выход":
#         print("Программа завершена. До свидания!")
#         break
#     elif цвет == "зеленый":
#         print("Можно идти.")
#     elif цвет == "желтый":
#         print("Подожди немного.")
#     elif цвет == "красный":
#         print("stop!")
#     else:
#         print("Неверный ввод. Введите: зеленый, желтый, красный или выход.")
#
"""как создаются функции"""
# from урок6 import surname


# определение наименование(параметры):
#       тело функции (логика функции)
#       возврашение обьекта(результат)

# наименование(АРГУМЕНТЫ)

# def funk_name():
#     print(f'name: {name} surname: {surname}')

# funk_name()


# def gat_birth_year(name: str, age: int) -> str:

# def func_name(name: str, age: int) -> str:
#     """Все работает"""
#     name = name.title()
#     age = 2025 - age
#     return f'name:{name} b_year:{age}'
#
# text = input('text your name and age')
# print(func_name('Avi', 19))
