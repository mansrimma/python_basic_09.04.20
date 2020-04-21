# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
# букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(str_lower):
    str_result = str_lower[0].upper() + str_lower[1:len(str_lower)-1]
    return str_result

user_words = input('Введите строку из латинских букв в нижнем регистре\n')
words_list = user_words.split()
result_word = []
for word in words_list:
    result_word.append(int_func(word))
print(' '.join(result_word))
