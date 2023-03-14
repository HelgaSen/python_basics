"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
str str(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)

    def get_total_income(self):
        return sum(self._income.values())


employee_1 = Position('Сергей', 'Петров', 'слесарь', 65000, 10000)
employee_2 = Position('Светлана', 'Иванова', 'кассир', 45000, 8000)
print(employee_1.get_full_name(), employee_1.position,
      employee_1.get_total_income(), sep=' | ')
print(employee_2.get_full_name(), employee_2.position,
      employee_2.get_total_income(), sep=' | ')
