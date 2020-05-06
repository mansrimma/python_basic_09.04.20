"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyError(Exception):
    def __init__(self, text):
        self.text = text

val_1 = int(input("input number: "))
try:
   val_2 = int(input("input number: "))
   if val_2 == 0:
       raise MyError('Division by zero')
except MyError as err:
    print(err)
else:
    tmp = val_1 / val_2
    print(tmp)
