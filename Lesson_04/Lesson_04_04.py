# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
#    Сформировать итоговый массив чисел, соответствующих требованию.
#    Элементы вывести в порядке их следования в исходном списке.
#    Для выполнения задания обязательно использовать генератор.

#    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#    Результат: [23, 1, 3, 10, 4, 11]


my_str = input('Введите числа через пробел: ')
my_list = my_str.split()
new_list = []

print(f'Исходный список: {my_list}')

for i in range(0, len(my_list)):
    count_list = [j for j in range(0, len(my_list)) if my_list[i] == my_list[j]]
    if len(count_list) == 1:
        new_list.append(my_list[i])
    count_list = []

print(f'Результат: {new_list}')