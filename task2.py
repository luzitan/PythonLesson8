"""
Задание 2. Сумма чисел
В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
программирования на языке Python.

Напишите программу, которая выводит на экран все строки этого файла в
обратном порядке.
Кстати, попробуйте открыть консоль Python и ввести команду import this.

Результат работы программы:
Namespaces are one honking great idea -- let's do more of those!
If the implementation is easy to explain, it may be a good idea.
If the implementation is hard to explain, it's a bad idea.
Although never is often better than *right* now.
"""

# zen = open("zen.txt", "r+")
#
# zenInverse = "\n".join([line for line in reversed(zen.read().split("\n"))])
# print(zenInverse)
# zen.close()

# Вариант 2

zen = open("zen.txt", "r+")
lines = zen.readlines()
zen.close()

for line in reversed(lines):
    print(line.strip())