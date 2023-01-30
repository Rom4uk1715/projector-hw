
# Task 1

  
from random import randint
import string
for char in string.ascii_uppercase:
    with open(char + '.kek', 'w') as f:
        c = str(randint(1, 100))
        f.write(str(c))
        with open('sumarry.txt', "a") as new_f:
            new_f.write(f.name + ":" + c + '\n')

# Task 2 
def task_2():

    with open('virsh.txt', "w+") as virsh2:
        virsh2.write("Тому що ніколи тебе не вирвеш\n"
                                            "ніколи не забереш,\n"
                                            "тому що вся твоя свобода\n"
                                            "складається з меж,\n"
                                            "тому що в тебе немає\n"
                                            "жодного вантажу,\n"
                                            "тому що ти ніколи не слухаєш,\n"
                                            "оскільки знаєш і так,\n"
                                            "що я скажу")

    with open('task2_file_with_some_content.txt', "r") as virsh2:
        virsh2upper = virsh2.read().upper()

    with open("task2_second_file.txt", 'w') as second_file_task_2:
        second_file_task_2.write(virsh2upper)

    return



# Task 3

import csv
import random
players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
results = []


for player in players:
    for i in range(100): # Перебираємо 100 варіантів гри один з одим 
        score = random.randint(0, 1000)
with open("results.csv", "w", newline='') as f:
    writer = csv.writer(f) # СТворити резулльтати
    writer.writerow(["Player name", "Score"])
    writer.writerows(results)

# Task 4 
import csv
from collections import defaultdict

high_scores = defaultdict(int)

with open("results.csv", "r") as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        player, score = row
        high_scores[player] = max(high_scores[player], int(score))
with open("high_scores.csv", "w", newline='') as f: # результат йщов у файл
    writer = csv.writer(f)
    writer.writerow(["Player name", "High Score"])
    for player, score in sorted(high_scores.items(), key=lambda x: x[1], reverse=True):
        writer.writerow([player, score])

# Task 5

height_list = []
weight_list = []
with open('hw (2) (1).csv', mode='r') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        height_list.append(float(row[' "Height(Inches)"']))
        weight_list.append(float(row[' "Weight(Pounds)"']))
        # print(row.keys())

avg_height = (sum(height_list) / len(height_list)) * 2.54
avg_weight = (sum(weight_list) / len(weight_list)) / 2.2046
print('avg of hight: ', avg_height, 'cm', '\navg of hight: ', avg_weight, 'kg')