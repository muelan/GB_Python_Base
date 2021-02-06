from abc import ABC, abstractmethod

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
#    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#    для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
#    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property


class Сlothing(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def amount_of_fabric ():
        pass


class Coat(Сlothing):

    @property
    def amount_of_fabric(self):
        amount = round(self.size/6.5 + 0.5, 2)
        print(f'Расход ткани на пальто {self.size} размера - {amount}')
        return amount


class Costume(Сlothing):

    @property
    def amount_of_fabric(self):
        amount = round(self.size * 2 + 0.3, 2)
        print(f'Расход ткани на костюм {self.size} роста -  {amount}')
        return amount


coat = Coat(42)
costume = Costume(4)

print(f'Общий расход ткани: {round(coat.amount_of_fabric + costume.amount_of_fabric, 2)}')
