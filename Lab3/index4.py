import math

n = int(input())
def pd(n):
    d = []
    while n % 2 == 0:
        d.append(2)
        n //= 2

    for i in range(3, int(math.isqrt(n)) + 1, 2):  

        while n % i == 0:
            d.append(i) 
            n //= i

    if n > 1:
        d.append(n)

    return d


print(pd(n))

        
