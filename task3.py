"""
Задача 3. Турнир
В файле first_tour.txt записано число K и данные об участниках турнира по
настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
первом туре. Во второй тур проходят участники, которые набрали более K
баллов в первом туре.
Напишите программу, которая выводит в файл second_tour.txt данные всех
участников, прошедших во второй тур, с нумерацией.
В первой строке нужно вывести в файл second_tour.txt количество участников
второго тура. Затем программа должна вывести фамилии, инициалы и
количество баллов всех участников, прошедших во второй тур, с нумерацией.
Имя нужно сократить до одной буквы. Список должен быть отсортирован по
убыванию набранных баллов.

Пример:
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Sergeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78
Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92
"""

def participants_second_tour():
    if int(el[2]) > passing_grade:
        lst = []
        lst.append(el[1][0] + ".")
        lst.append(el[0])
        lst.append(str(el[2]))
        list_second_tour.append(lst)
    return list_second_tour

def write_second_tour():
    second_tour = open('second_tour.txt', 'w+')
    second_tour.write(str(len(strs_second_tour)) + "\n")
    for i in range(1, len(strs_second_tour) + 1):
        second_tour.write(f"{i}) {strs_second_tour[i-1]}\n")
    second_tour.close()

# открываем файл и получаем данные
first_tour = open('first_tour.txt', 'r+')
read_txt = first_tour.readlines()
first_tour.close()

# обрабатываем данные, получаем список
list_first_tour = []
passing_grade = int(read_txt[0])
list_participants = read_txt[1:]
for el in list_participants:
    el = el.strip().split()
    list_first_tour.append(el)

# формируем список второго тура
list_second_tour = []
for el in list_first_tour:
    list_second_tour = participants_second_tour()

# сортируем список второго тура
list_second_tour.sort(key=lambda x: x[2], reverse=True)

# меняем тип последнего элемента на str
for i in range(len(list_second_tour)):
    list_second_tour[i][2] = str(list_second_tour[i][2])
# сшиваем двумерный массив в одномерный
strs_second_tour = []
for el in list_second_tour:
    strs_second_tour.append(" ".join(el))

# сохраняем список второго тура в файл
write_second_tour()

"""
Второй вариант
"""

# # Открываем файл first_tour.txt для чтения
# with open("first_tour.txt", "r") as file:
#     lines = file.readlines()
#     # Первая строка содержит число K
#     K = int(lines[0])
#     # Словарь для хранения данных участников
#     participants = {}
#     # Словарь для хранения участников, прошедших во второй тур
#     filter_player = {}
#     count = 1
# # Обрабатываем оставшиеся строки
# for line in lines[1:]:
#     # Разделяем строку на части
#     data = line.strip().split()
#     # Формируем имя участника с инициалом
#     name = f"{data[1][0]}. {data[0]}"
#     # Получаем количество баллов
#     score = int(data[-1])
#     # Сохраняем участника и его баллы
#     participants[name] = score
# # Фильтруем участников, набравших более K баллов
# for player, score in participants.items():
#     if score > K:
#         filter_player[player] = score
#
# # Сортируем участников по убыванию баллов
# sorted_filter_player = dict(sorted(filter_player.items(), key=lambda x: x[1], reverse=True))
# # Открываем файл second_tour.txt для записи
# with open("second_tour.txt", "w") as file:
#     # Записываем количество участников второго тура
#     file.write(f"{len(sorted_filter_player)}\n")
#     # Записываем данные участников с нумерацией
#     for player, score in sorted_filter_player.items():
#         file.write(f"{count}) {player} {score}\n")
#         count += 1
