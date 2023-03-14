"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self.weight = None
        self.depth = None

    def calc_material_required(self):
        return (self._length * self._width * self.weight * self.depth) / 1000


road_param = Road(20, 5000)
road_param.weight = 25
road_param.depth = 0.05
print(f'Понадобится {road_param.calc_material_required()} т асфальта')