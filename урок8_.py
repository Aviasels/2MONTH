# Контекстный менеджер "witth", работа с файлами
# a - add (запись, дозапись)
# w - write(запись, перезапись)
# r - read (чтение)
# x - проверка названия перед созданием

from time import sleep

with open('new_file.txt', 'r') as file:
    for i in file.readlines():
        print(i, end='')
        sleep(2)

        # print(file.readlines())
        # print(file.read())

# with open('new_file.txt', 'a') as file:
#     file.write("Бишкек")

# file = open('new_file.txt', 'w')
# file.write('Ташмамат кызы Арууке')
# file.close()

