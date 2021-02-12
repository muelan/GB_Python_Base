# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#    В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
#    и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
#    месяца и года (например, месяц — от 1 до 12).
#    Проверить работу полученной структуры на реальных данных.

class Date():
    def __init__(self, date_in):
        self.date_in = date_in


    @classmethod
    def date_to_digit(cls, date_in):
        my_date = []
        my_date_help = date_in.split('-')
        for el in my_date_help:
            if el != '-':
                my_date.append(int(el))
        return my_date


    @staticmethod
    def date_valid(date_list):
        month_31 = [1, 3, 5, 7, 8, 10, 12]
        month_30 = [4, 6, 9, 11]
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        k = 1

        if not(year in range(1600, 2101)):
            k = 0
            print('Год введен неправильно. Диапазон ввода 1600-2100 гг.')
        if not(month in range(1, 13)):
            k = 0
            print('Месяц введен неправильно.')

        if (month in month_31) and not (day in range(1, 32)):
            k = 0
            print(month)
            print('День введен неправильно. В этом месяце 31 день.')
        elif (month in month_30) and not (day in range(1, 31)):
            k = 0
            print('День введен неправильно. В этом месяце 30 дней.')
        elif (month == 2) and (not (day in range(1, 29))) and (year % 4 != 0):
            k = 0
            print('День введен неправильно. В феврале этого года 28 дней.')
        elif (month == 2) and (not (day in range(1, 30))) and (year % 4 == 0):
            k = 0
            print('День введен неправильно. В феврале этого года 29 дней.')

        if k == 1:
            print('Данные введены верно.')

        return



date_in = input('Введите дату в формате "дд-мм-гггг": ')

date = Date(date_in)
print(f'Дата в целочисленном виде: {date.date_to_digit(date_in)}')
Date.date_valid(date.date_to_digit(date_in))



