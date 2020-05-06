"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
 строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
 декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип
  к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
  месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
  реальных данных.
"""

class Data:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = str(dd_mm_yy)

    @classmethod
    def date_numb(cls, dd_mm_yy):
        d = [int(s) for s in dd_mm_yy.split('-')]
        return d

    @staticmethod
    def valid_date(date):
        try:
            day = date[0]
            if day > 31:
                raise Exception ('День должен быть от 1 до 31')
        except Exception as err:
            print(err)
        else:
            print('День:', day, end=' ')
        try:
            month = date[1]
            if 0 <= month > 12:
                raise Exception('Месяц должен быть от 1 до 12')
        except Exception as err:
            print(err)
        else:
            print('Месяц:', month, end=' ')
        try:
            year = date[2]
            if 0 <= year > 2020:
                raise Exception('Год должен быть от 1 до 2020')
        except Exception as err:
            print(err)
        else:
            print('Год:', year, end=' ')

    def __str__(self):
        return f'Текущая дата {Data.date_numb(self.dd_mm_yy)}'

user_day = Data('15-05-2020')
print(user_day)
print(Data.valid_date([36, 5, 2020]))
print(Data.valid_date([25, 13, 2020]))
print(Data.valid_date([25, 11, 2021]))
