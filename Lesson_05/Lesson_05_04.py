# -*- coding: utf-8 -*-

#4. Создать (не программно) текстовый файл со следующим содержимым:
#    One — 1
#    Two — 2
#    Three — 3
#    Four — 4
#    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#    При этом английские числительные должны заменяться на русские.
#    Новый блок строк должен записываться в новый текстовый файл.

num_list = [['1', 'One', 'Один'], ['2', 'Two', 'Два'], ['3', 'Three', 'Три'], ['4', 'Four', 'Четыре']]
num_list_out = []

with open('my_file_content_04.txt') as my_file:
    num_list_in = my_file.readlines()

i = 0
while i < len(num_list_in):
    num_list_in[i] = list(num_list_in[i].split())
    num_list_in[i][0] = num_list[i][2]
    num_list_out.append(' '.join(num_list_in[i]))
    i += 1

with open('my_file_content_04_out.txt', 'w', encoding="utf-8") as my_file_out:
    for el in num_list_out:
        my_file_out.write(el + '\n')

