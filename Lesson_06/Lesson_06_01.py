# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
#    красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
#    2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
#    в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
#    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
#    сообщение и завершать скрипт.

import time

class TrafficLight:


    def running (self):
        __color = [('красный', '7'), ('желтый', '2'), ('зеленый', '10')]

        for i in range(0, len(__color)):
            time_count = int(__color[i][1])
            for j in range(time_count, 0, -1):
                print(f'{__color[i][0]} %d' % j)
                time.sleep(1)


a = TrafficLight()
a.running()



