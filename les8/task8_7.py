"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
 перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
 класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
 полученного результата.
"""

class ComplexNuber:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        return f'Сумма равна: {x} + {y}i'

    def __mul__(self, other):
        x = self.a * other.a - self.b * other.b
        y = self.a * other.b + self.b * other.a
        return f'Произведение равно: {x} + {y}i'


z_1 = ComplexNuber(1, 2)
z_2 = ComplexNuber(2, 3)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
