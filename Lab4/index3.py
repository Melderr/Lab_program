import random

random_numbers = [[random.randint(5, 61) for _ in range(5)] for _ in range(5)]

def qs(rn):
    
    if len(rn) <= 1:
        return rn

    first = rn[len(rn) // 2][0]
    
    left = [x for x in rn if x[0] < first]
    middle = [x for x in rn if x[0] == first]
    right = [x for x in rn if x[0] > first]

    return qs(left) + middle + qs(right)

print(qs(random_numbers))
