import random

mas = [random.randint(0, 100) for _ in range(10)]
for i in range(len(mas)):
    for j in range(i + 1, len(mas)):
        max_ind = i
        if mas[j] > mas[max_ind]:
            max_ind = j
        if max_ind != i:
            mas[i], mas[max_ind] = mas[max_ind], mas[i]
            
print(mas)
