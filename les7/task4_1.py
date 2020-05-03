"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, list_val):
        self.list_val = list_val

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_val]))

    def __add__(self, other):
        list_sum = []
        list_res = []
        for i in range(len(self.list_val)):
            for j in range(len(self.list_val[0])):
                summ = self.list_val[i][j] + other.list_val[i][j]
                list_sum.append(summ)
            list_res.append(list_sum)
            list_sum = []
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in list_res]))

l = Matrix([[2, 3], [4, 5], [6, 7]])
l_2 = Matrix([[0, 4], [3, 2], [8, 8]])
x = l + l_2
print(x)
