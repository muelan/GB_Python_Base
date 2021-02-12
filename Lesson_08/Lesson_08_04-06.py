# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
#    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#    В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
#    уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
#    и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве
#    единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
#    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
#    изученных на уроках по ООП.

"""
На данный момент паратры в классе Warehouse (склад) формальны.


"""


class Warehouse():
    def __init__ (self, model, price, quantity):
        #self.id = 0                            # id товара
        self.model = model                      # Модель товара
        self.price = price                      # Цена товара
        self.quantity = quantity                # Количесиво товара
        self.subdivision = ['Отдел 1', 'Отдел 2', 'Отдел 3']          # Подразделения организации


    """Прием товара на склад"""

    @classmethod
    def arrival_of_goods(self):
        goods_list_in = []                  # Список товаров на складе
        print('Прием товара на склад...')
        while True:
            try:
                model = input('Наименование: ')
                price = round(float(input('Цена: ')), 2)
                quantity = int(input('Количество: '))
                goods_list_in.append({'Модель': model, 'Цена': price, 'Количество': quantity})
                print(f'Текущий товар на складе -\n {goods_list_in}')
            except:
                print('Ошибка ввода данных')
            print(f'\nДля выхода из "Приема товара" - Q, продолжение - любая клавиша...')
            out = input()
            if out == 'Q' or out == 'q' or out == 'Й' or out == 'й':
                break
        return goods_list_in



    """Перемещение товара со склада на подразделение"""

    @classmethod
    def movement_of_goods(self, goods_list_in):
        goods_list_move = []                            # Список пермещенных товаров
        print('\nПеремещение со склада...')
        while True:
            try:
                model = input('Наименование перемещаемой единицы: ')
                quantity = int(input('Количество: '))
                subdivision = input('Подразделение: ')
                goods_list_move.append({'Модель': model, 'Количество': quantity, 'Подразделение': subdivision})

                """Проверка на количество (перемещаемое и остатки на складе)"""
                for i in range(0, len(goods_list_in)):
                    if (goods_list_in[i].get('Модель') == model) and (goods_list_in[i].get('Количество') > quantity):
                        goods_list_in[i].update({'Модель': model, 'Цена': goods_list_in[i].get('Цена'),
                                                 'Количество': goods_list_in[i].get('Количество') - quantity})
                    elif (goods_list_in[i].get('Модель') == model) and (goods_list_in[i].get('Количество') == quantity):
                        goods_list_in.pop(i)
                    elif (goods_list_in[i].get('Модель') == model) and (goods_list_in[i].get('Количество') < quantity):
                        print(
                            f'Количество больше остатка. На остатке {goods_list_in[i].get("Количество")} единиц товара')
                        break
                """-------------------------------------------------------"""

                print(f'Текущий товар на складе -\n {goods_list_in}')
            except:
                print('Ошибка ввода данных')
            print(f'\nДля выхода - Q, продолжение - любая клавиша...')
            out = input()
            if out == 'Q' or out == 'q' or out == 'Й' or out == 'й':
                return goods_list_in


class Office_equipment(Warehouse):
    def __init__ (self, model, year, color, format, resolution, speed):
        self.model = model                      # Модель товара
        self.year = year                        # Год выпуска
        self.color = color                      # Цветность печати
        self.format = format                    # Максимальный формат печати
        self.resolution = resolution            # Разрешение печати
        self.speed = speed                      # Скорость печати


class Printer(Office_equipment):
    def __init__ (self):
        self.type = type                        # Тип принтера (лазерный, струйны...)


class Scaner(Office_equipment):
    def __init__(self, type, optical, color_depth):
        self.type = type                        # Тип сканера (планшетный...)
        self.optical = optical                  # Оптическая плотность
        self.color_depth = color_depth          # Глубина цвета


class Xerox(Office_equipment):
    def __init__(self, capacity):
        self.capacity = capacity                # Емкость фотобарабана



goods_list_in = Warehouse.arrival_of_goods()
print(Warehouse.movement_of_goods(goods_list_in))

