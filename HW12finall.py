'''1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
To each file append a random number between 1 and 100.
Create a summary file (summary.txt) that contains name of the file and number in that file:
A.txt: 67
B.txt: 12
Z.txt: 98'''

# Task 1

  
from random import randint
import string
for char in string.ascii_uppercase:
    with open(char + '.kek', 'w') as f:
        c = str(randint(1, 100))
        f.write(str(c))
        with open('sumarry.txt', "a") as new_f:
            new_f.write(f.name + ":" + c + '\n')

# TAsk 2 
content = [
    'Тому що ніколи тебе не вирвеш\n',
    'ніколи не забереш,\n',
    'тому що вся твоя свобода\n',
    'складається з меж,\n',
    'тому що в тебе немає\n',
    'жодного вантажу,\n',
    'тому що ти ніколи не слухаєш,\n',
    'оскільки знаєш і так,\n',
    'що я скажу.\n']

for i in content:
    with open('content_file.txt', mode="w", encoding="utf-8") as file, open('copy_content.txt', mode='a', encoding="utf-8") as f:
        file.writelines(content)
        f.writelines(i.upper())