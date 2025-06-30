"""
Задача 5*. «Война и мир»
Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это
довольно объёмное произведение лежит в архиве voina-i-mir.zip. Напишите
программу, которая подсчитывает статистику по буквам (не только русского
алфавита) в этом романе и выводит результат на экран (или в файл). Результат
должен быть отсортирован по частоте встречаемости букв (по возрастанию или
убыванию). Регистр символов имеет значение.
Архив можно распаковать вручную, но, если хотите, можете изучить
документацию по модулю zipfile (можно использовать и другой модуль) и
попробовать написать код, который будет распаковывать архив за вас.
"""

import zipfile

with zipfile.ZipFile('voina-i-mir.zip', 'r') as zip_ref:
    zip_ref.extractall()

voina_i_mir = open('voyna-i-mir.txt', 'r+', encoding='utf-8')
lst = voina_i_mir.readlines()
voina_i_mir.close()

words = {}
for line in lst:
    for char in line:
        if char.isalpha():
            if char not in words:
                words[char] = 1
            else:
                words[char] += 1

count = sum(words.values())
words_fraction = {key: round(value/count, 3) for key, value in words.items()}

sort_words = dict(sorted(words_fraction.items(), key=lambda x: (-x[1], x[0])))

with open('res-word-voyna-i-mir.txt', 'w+', encoding='utf-8') as file:
    for key, value in sort_words.items():
        file.write(f'{key} {value}\n')
