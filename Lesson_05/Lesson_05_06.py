# -*- coding: utf-8 -*-

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#    практических и лабораторных занятий по этому предмету и их количество.
#    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#    Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.


with open('my_file_content_06.txt', 'r',  encoding="utf-8") as my_file:
    my_list_in = my_file.readlines()

print(f'Начальный список\n{my_list_in}')


""" Блок удаления лишних символов - остаются только названия (str) и числа (int) """
i = 0
while i < len(my_list_in):
    my_list_in[i] = list(my_list_in[i].split())
    j = 0
    while j < len(my_list_in[i]):
        if j == 0:
            my_list_in[i][j] = my_list_in[i][j][:-1]
        else:
            for char_in in my_list_in[i][j]:
                n = 0
                while n < len(char_in):
                    if not(ord(char_in[n]) in range(48, 58)):
                        my_list_in[i][j] = my_list_in[i][j].replace(char_in[n], '')
                    n += 1
            if my_list_in[i][j] == '':
                my_list_in[i][j] = 0
            else:
                my_list_in[i][j] = int(my_list_in[i][j])
        j += 1
    i += 1
print(f'\nПромежуточный список\n{my_list_in}')
"""===================================================================="""

my_dict = {my_list_in[i][0]: my_list_in[i][1]+my_list_in[i][2]+my_list_in[i][3] for i in range(0, len(my_list_in))}

print(f'\nРезультат\n{my_dict}')