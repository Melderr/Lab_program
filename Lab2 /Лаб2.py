#2.1
import random

a = []
for i in range(10):
    a.append(random.randint(2, 103))

for i in range(len(a) - 1):
    m = i
    for j in range(i + 1, len(a)):
        if a[j] < a[m]:
            m = j
    a[i], a[m] = a[m], a[i]

print(a)
#2.2
import random

a = []
for i in range(10):
    a.append(random.randint(0, 100))

for i in range(len(a) - 1):
    m = i
    for j in range(i + 1, len(a)):
        if a[j] > a[m]:
            m = j
    a[i], a[m] = a[m], a[i]

print(a)
#2.3
a = ["23-45-67", "34-95-21", "50-32-66", "24-63-05"]

for i in range(len(a) - 1):
    m = i
    for j in range(i + 1, len(a)):
        if a[j] < a[m]:
            m = j
    a[i], a[m] = a[m], a[i]

print(a)
