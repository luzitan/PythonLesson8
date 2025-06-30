"""
Задача 4. Частотный анализ
Есть файл text.txt, который содержит текст. Напишите программу, которая
выполняет частотный анализ, определяя долю каждой буквы английского
алфавита в общем количестве английских букв в тексте, и выводит результат в
файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
учитывать не нужно.
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
тремя знаками в дробной части. Буквы должны быть отсортированы по
убыванию их доли. Буквы с равной долей должны следовать в алфавитном
порядке.

Пример:
Содержимое файла text.txt:
Mama myla ramu.

Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083
"""


text = open('text.txt', 'r+')
str_text = text.read().lower()
text.close()

dict_letters = {}

for char in str_text:
    if char.isalpha():
        if char not in dict_letters:
            dict_letters[char] = 1
        else:
            dict_letters[char] += 1

count = sum(dict_letters.values())
for key, value in dict_letters.items():
    dict_letters[key] = round(value/count, 3)


sort_dict = dict(sorted(dict_letters.items(), key=lambda x: (-x[1], x[0])))

analysis = open('analysis.txt', 'w+')
for key, value in sort_dict.items():
    analysis.write(f'{key} {value}\n')

analysis.close()
