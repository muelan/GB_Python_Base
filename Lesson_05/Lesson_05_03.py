# -*- coding: utf-8 -*-

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#    Выполнить подсчет средней величины дохода сотрудников.

sum_money = 0
min_money = 20000


with open('my_file_content_03.txt', 'r', encoding="utf-8") as f_obj:
    people_list = f_obj.readlines()

i = 0
n = 0
print(f'Спислк сотрудник с окладом менmше {min_money} руб.:')
while i < len(people_list):
    people_list[i] = people_list[i].split()
    if int(people_list[i][1]) < min_money:
        n = 1
        print(str(people_list[i][0]))
    sum_money = sum_money + int(people_list[i][1])
    i += 1

if n ==0:
    print('Список пуст')
print('\nСредний доход сотрудников: {:.2f}'.format(sum_money/(i)))
