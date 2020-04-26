"""
5. Создать (программно) текстовый файл, записать в него программно набор
 чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел
 в файле и выводить ее на экран.
"""

with open('new_file5.txt', 'w', encoding='UTF-8') as file:
    user_number = input('Введите числа через пробел:\n')
    file.write(user_number)

with open('new_file5.txt', 'r', encoding='UTF-8') as file:
    content = file.read()
    number_list = [int(el) for el in content.split()]
    print('Сумма чисел:', sum(number_list))
