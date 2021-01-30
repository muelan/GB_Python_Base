# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
#    который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
#    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
#    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#    Выполните вызов методов и также покажите результат.

class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return '{} поехала'.format(self.name)

    def stop(self):
        return '{} остановилась'.format(self.name)

    def turn_right(self):
        return '{} повернула направо'.format(self.name)

    def turn_left(self):
        return '{} повернула налево'.format(self.name)

    def turn_back(self):
        return '{} сдала назад'.format(self.name)

    def show_speed(self):
        return 'Текущая скорость автомобиля {0} - {1} км/ч'.format(self.name, self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость автомобиль {self.name} - {self.speed} км/ч. Превышение скорости!'


class SportCar(Car):
    def auto_method(self):
        print("Спортивный автомобиль")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость автомобиль {self.name} - {self.speed} км/ч. Превышение скорости!'
        else:
            return f'Автомобиль {self.name} едет с допустимой скоростью {self.speed} км/ч.'

class PoliceCar(Car):
    def auto_method(self):
        if self.is_police == True:
            return 'Полицейский автомобиль'



lada = TownCar(50, 'Зеленый', '"Лада"', False)
ferari = SportCar(200, 'Красный', '"Ферари"', False)
kamaz = WorkCar(60, 'Синий', '"Камаз"', False)
bmw = PoliceCar(110, 'Серый', '"BMW"', True)

print(f'Если едет {bmw.name} ({bmw.auto_method()}), то {lada.turn_right()}, {kamaz.stop()}, {ferari.go()}')
print('\nАвто в городе...')
print(f'{lada.show_speed()}')
print(f'{kamaz.show_speed()}')



