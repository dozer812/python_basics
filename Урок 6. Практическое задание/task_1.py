"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:

    # метод класса
    def __init__(self, color):
        self._color = color  # определяем приватный атрибут класса

    # метод класса
    def running(self):
        for key, value in self._color.items():
            print(f"Цвет: {key}, Время: {value}")
            sleep(value)


obj = TrafficLight(color={
    "Красный": 7,
    "Желтый": 2,
    "Зеленый": 7})
obj.running()
