#4.1

import random

a = [random.randint(-1000, 1000) for i in range(1000)]

def qs(a):
    if len(a) <= 1:
        return a

    b = a[len(a) // 2]
    c = [x for x in a if x < b]
    d = [x for x in a if x == b]
    e = [x for x in a if x > b]

    return qs(c) + d + qs(e)

print(qs(a))


#4.2

import random

a = [random.randint(50, 100) for i in range(30)]

def qs(a):
    if len(a) <= 1:
        return a

    b = a[len(a) // 2]
    c = [x for x in a if x < b]
    d = [x for x in a if x == b]
    e = [x for x in a if x > b]

    return qs(c) + d + qs(e)

print(qs(a))


#4.3

import random

a = [[random.randint(5, 61) for j in range(5)] for i in range(5)]

def qs(a):
    if len(a) <= 1:
        return a

    b = a[len(a) // 2][0]
    c = [x for x in a if x[0] < b]
    d = [x for x in a if x[0] == b]
    e = [x for x in a if x[0] > b]

    return qs(c) + d + qs(e)

a = qs(a)

for b in a:
    print(b)


#4.4

a = [
    "Васильев","Кузнецов","Фёдоров","Соколов","Смирнов","Новиков","Соловьёв","Павлов","Романов","Степанов","Волков","Козлов"
]

a.sort()

print(a)
