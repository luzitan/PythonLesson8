"""
Задание 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, которые могут быть
разделены пробелами и концами строк. Напишите программу, которая выводит
сумму чисел в выходной файл answer.txt.
"""
numbers = open("numbers.txt", "r+")
sumN = sum(list(map(int, numbers.read().split())))
numbers.close()

answer = open("answer.txt", "w+")
answer.write(str(sumN))
answer.close()