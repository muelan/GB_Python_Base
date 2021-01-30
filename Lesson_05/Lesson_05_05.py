# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


sum_list = 0

in_str = input('Введите набор чисел, разделенных пробелами: ')
with open('my_file_py_05.txt', 'w') as my_file_out:
    my_file_out.write(in_str)

with open('my_file_py_05.txt') as my_file_out:
    digit_list = my_file_out.readline().split()

for el in digit_list:
    sum_list = sum_list + int(el)

print(f'Сумма чисел: {sum_list}')