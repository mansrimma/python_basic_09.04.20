# 4. Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

n = int(input('Введите целое положительное число: '))

max = 0
while n != 0:
    digit = n % 10
    if digit > max:
        max = digit
    n = n // 10
print('Наибольшая цифра: ', max)
