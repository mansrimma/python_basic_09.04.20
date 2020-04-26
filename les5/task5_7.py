"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором
каждая строка должна содержать данные о фирме: название, форма собственности,
выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
"""

with open('new_file7.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()

new_content = []
for el in content:
    for itm in el.split():
        if itm.isdigit():
            new_content.append(int(itm))
        else:
            new_content.append(itm)
print(new_content)
