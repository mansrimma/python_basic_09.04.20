# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты
# и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

sec = int(input('Введите время в секундах: '))
hour = sec // 360
minute = (sec - hour*360) // 60
sec = sec % 60
print(hour, minute, sec, sep=':')
