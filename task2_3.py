#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
# к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

while True:
    user_month = input('Введите число от 1 до 12: ')
    if user_month.isdigit():
        user_month = int(user_month)
        break
    else:
        print('Ошибка ввода, это не число')

for key in month.keys():
    if user_month in month.get(key):
        print(key)
