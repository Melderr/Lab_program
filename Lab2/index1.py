import random

mas = [random.randint(2, 103) for _ in range(10)]
for i in range(len(mas)):
    for j in range(i + 1, len(mas)):
        min_ind = i
        if mas[j] < mas[min_ind]:
            min_ind = j
        if min_ind != i:
            mas[i], mas[min_ind] = mas[min_ind], mas[i]
            
print(mas)
