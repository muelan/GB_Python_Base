# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
#    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
#    В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
#    вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
#    только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
#    соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
# нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.

class Cell():

    def __init__(self, number):
        self.number = int(number)


    def __str__(self):
        return f'Результат операции {self.number * "*"}'


    def __add__(self, other):
        res_str = (self.number + other.number) * "*"
        return f'Результат операции СЛОЖЕНИЕ: {res_str} ({self.number + other.number})'


    def __sub__(self, other):
        if (self.number - other.number) > 0:
            res_str = (self.number - other.number)* "*"
        else:
            res_str = 'Вычитание клеток невозмлжно!'
        return f'Результат операции ВЫЧИТАНИЕ: {res_str} ({self.number - other.number})'


    def __mul__(self, other):
        res_str = (self.number * other.number) * "*"
        return f'Результат операции УМНОЖЕНИЕ: {res_str} ({self.number * other.number})'


    def __truediv__(self, other):
        res_str = int(round(self.number / other.number)) * "*"
        return f'Результат операции ДЕЛЕНИЕ: {res_str} ({int(round(self.number / other.number))})'

    @classmethod
    def make_order(self, a, cell_row):
        row_str = ''
        for i in range(int(a.number / cell_row)):
            row_str += f'{"*" * cell_row} \n'
        row_str += f'{"*" * (a.number % cell_row)}'
        return f'\n"Построение клетки" по {cell_row} из {a.number} ячеек: \n{row_str} '


c_1 = Cell(30)
c_2 = Cell(9)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(Cell.make_order(c_1, 7))
print(Cell.make_order(c_2, 5))
