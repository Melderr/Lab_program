import random

random_numbers = [random.randint(50, 100) for _ in range(30)]

def bubble_sort(rn):
    
    n = len(rn)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rn[j] > rn[j + 1]:
                rn[j], rn[j + 1] = rn[j + 1], rn[j]
                
    return rn

print(bubble_sort(random_numbers))
