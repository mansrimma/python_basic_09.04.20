"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, v, h):
        self.name = name
        self.v = v
        self.h = h

    @abstractmethod
    def square(self):
        pass

    @property
    def get_square(self):
        return (self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)


class Coat(Clothes):
    def __init__(self, name, v, h=0):
        super(Coat, self).__init__(name, v, h)

    def square(self):
        return f'Расход ткани на пальто {self.v / 6.5 + 0.5}'


class Suit(Clothes):
    def __init__(self, name, h, v=0):
        super(Suit, self).__init__(name, v, h)

    def square(self):
        return f'Расход ткани на костюм {self.h * 2 + 0.3}'


coat1 = Coat('coat', 56)
suit1 = Suit('suit', 175)

print(coat1.square())
print(suit1.square())
