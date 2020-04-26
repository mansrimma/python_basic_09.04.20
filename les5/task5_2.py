"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('new_file2.txt', 'r') as file:
    content = file.readlines()
    for ind, itm in enumerate(content, 1):
        count_word = itm.count(' ') + 1
        print(ind, 'строка, слов в строке:', count_word)
