# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
#    реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
#    создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#    Проверьте корректность полученного результата.

class ComplexDigit():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма комплексных чисел: ')
        return f'({self.a} + {self.b}i) + ({other.a} + {other.b}i) = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел: ')
        return f'({self.a} + {self.b}i) * ({other.a} + {other.b}i) = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


с1 = ComplexDigit(5, -1)
с2 = ComplexDigit(-4, 3)
print(f'Первое число: {с1}')
print(f'Второе число: {с2}')
print(с1 + с2)
print(с1 * с2)