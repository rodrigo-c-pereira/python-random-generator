import random

numbers_set = set()

for i in range(6):
    n = random.randint(1,60)

    while n in numbers_set:
        n = random.randint(1,60)

    numbers_set.add(n)
    print(n)