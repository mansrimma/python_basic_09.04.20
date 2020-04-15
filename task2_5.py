#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

while True:
    user_numb = input('Введите целое число: ')
    if user_numb.isdigit():
        user_numb = int(user_numb)
        break
    else:
        print('Ошибка ввода, это не число')

pos = 0
while pos < len(my_list) and my_list[pos] >= user_numb:
    pos += 1
my_list.insert(pos, user_numb)
print(my_list)
