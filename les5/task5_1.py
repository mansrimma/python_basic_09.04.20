"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

f = open('my_txt.txt', 'w')

while True:
    user_str = input('Введите строку:\n')
    if user_str:
      with open('my_txt.txt', 'a') as file:
          file.write(user_str + '\n')
    else:
        break
