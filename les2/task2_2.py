#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input()

while True:
    user_numb = input('Введите количество элементов списка: ')
    if user_numb.isdigit():
        user_numb = int(user_numb)
        break
    else:
        print('Ошибка ввода, это не число')

user_list = []
for itm in range(user_numb):
    user_list.append((input('Введите элемент списка: ')))

for i in range(1, user_numb, 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]
print(user_list)
