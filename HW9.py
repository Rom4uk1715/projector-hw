"""You have 100 cats.

One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, 
always starting at the same spot, with the first cat (cat # 1). 
Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

The first round, you stop at every cat, placing a hat on each one.
The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.

Optional: Make function that can calculate hat with any amount of rounds and cats.

Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. Code is simple here, but you might struggle with algorithm. Therefore don`t try to write a code from the first attempt. """

allcats = 100
alllaps = 100
hatscats = []

for kolo in range(1, alllaps + 1): # Пребираємо по колу в діапазоні від 1 до 100
    for cat1 in range(1, allcats + 1): # Перебираємо всіх котів по колу

        # zupeniajoms na n koti
        if cat1 % kolo == 0: # якщо кіт може поділитись без остачі на коло (jaksho cat2/kolo 1 propuisk todi cat/2 = 0 zdijsnuemo)
            if cat1 in hatscats: #jaksho v kota je shlapa 
                hatscats.remove(cat1) # znimajemo ii
            else:
               hatscats.append(cat1) # nadivajemo jiji
        else:
            pass # propuskajemo kota

print(len(hatscats))

