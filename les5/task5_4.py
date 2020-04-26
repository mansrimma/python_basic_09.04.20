"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
 построчно данные. При этом английские числительные должны заменяться на
 русские. Новый блок строк должен записываться в новый текстовый файл.
"""

dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('new_file4.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    new_content = []
    for el in content:
        s = el[:el.find(' ')]
        if s in dict.keys():
            el = dict.get(s) + el[el.find(' '):]
        new_content.append(el)

with open('new_file4_1.txt', 'w', encoding='UTF-8') as file:
    file.writelines(new_content)
