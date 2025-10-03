# Lambda функции. Обработки исключений.
# try:
#     print(2 + 4)
# except:
#     print('обнаружена ошибка')
# else:
#     print('ошибок не найдено')
# finally:
#     print('проверка завершена')



# students = [2, 3, 4, 6, 7, 9, 10, 12, 13]
# total = 0

# while students:
#     try:
#         test_result = int(input(f'student №{students[0]} '))
#         total += test_result
#         del students[0]
#         print(total)
#         print(f'{total} in {students_count * 40}')
#         print({total} / students_count )
#     except:
#         print('вводите только числа!')


# print(name)
# print(int('python'))
# print(2 + 'kg')
# print([1, 2, 3][9])

# lambda_func = lambda n1, n2: n1 + n2
# print(lambda_func(2, 4))
# print(type(lambda_func))

#
# def def_func(n1, n2):
#      return n1 + n2
#      print(def_func(2, 4))
#  print(type(def_func))



# def up_first_letter(word: str) -> str:
#      return word.title()
#
#
# def show_words(func, words):
#      for i in words:
#          print(func(i))

# show_words(up_first_letter, ['london', 'paris', 'rome'])
# show_words(lambda word: word.title(),['london', 'paris', 'rome'])
# show_words(len, ['adil', 'arsen', 'alim'])

# sorted, filter, map
# cities = ['london', 'paris', 'rome' 'barselona']
# print(cities)


# filter_cities = list(filter(lambda word: len(word) >= 6, cities))
# print(filter_cities)

# cities = ['london', 'paris', 'rome', 'barselona']
# print(cities)

# sorted_cities = sorted(cities)
# print(sorted_cities)
#
# sorted_cities = sorted(cities, key=lambda word: word[-1])
# print(sorted_cities)


# Lambda функция. Обработка исключений.

lambda_func = lambda n1, n2: n1 + n2
print(lambda_func(2, 3))
print(type(lambda_func))


