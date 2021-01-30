# -*- coding: utf-8 -*-

# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
#    вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

content = ' '

print('Введите данные в файл:')

with open('my_file_py_01.txt', 'w', encoding="utf-8") as my_file:
    while content != '':
        content = input()
        print(f'{content}', file=my_file)


