# -*- coding: utf-8 -*-
import json

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#    название, форма собственности, выручка, издержки.
#    Пример строки файла: firm_1 ООО 10000 5000.
#    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#    Если фирма получила убытки, в расчет средней прибыли ее не включать.
#    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#    Итоговый список сохранить в виде json-объекта в соответствующий файл.

my_str_in = ' '
my_list_in = []

""" ПОдготовка списка из файла для расчетов"""

with open('my_file_content_07.txt', 'r',  encoding="utf-8") as my_file:
    while my_str_in != '':
        my_str_in = my_file.readline()
        print(my_str_in)
        my_list_in.append(my_str_in.split())


"""Формирование списков: 1. Названия фирм и 2. Прибыль/убытки по фирмам
   Вычисление средней пибыли"""
i = 0
sum = 0
counnt = 0
firm_lıst = []
proceeds_list = []

while i < len(my_list_in)-1:
    firm_lıst.append(my_list_in[i][0])
    proceeds_list.append(int(my_list_in[i][2]) - int(my_list_in[i][3]))
    if proceeds_list[i] >= 0:
        sum += proceeds_list[i]
    else:
        counnt += 1
    i += 1

average_profit = sum/(len(proceeds_list) - counnt)
print('\nСредняя прибыль предприятий: {:.2f}'.format(average_profit))


""" Формирование списка"""
my_list_out = [dict(zip(firm_lıst, proceeds_list)), {'average_profit': round(average_profit, 2)}]
print(f'\nРезультат: {my_list_out}')

with open('my_file.json', 'w') as write_f:
    json.dump(my_list_out, write_f)