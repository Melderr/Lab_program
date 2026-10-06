import random

random_numbers = [random.randint(-1000, 1000) for _ in range(1000)]

def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

print(bubble_sort(random_numbers))
