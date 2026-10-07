#3.1
def f1(n):
    if n > 0:
        f1(n - 1)
        print(n)

n = int(input())
f1(n)

#3.2
def f2(a, b):
    print(a)
    if a < b:
        f2(a + 1, b)
    elif a > b:
        f2(a - 1, b)

a = int(input())
b = int(input())
f2(a, b)

#3.3
def f3(n):
    if n == 0:
        return 0
    return n % 10 + f3(n // 10)

n = int(input())
print(f3(n))

#3.4
def f4(n, k=2):
    if n == 1:
        return
    if n % k == 0:
        print(k)
        f4(n // k, k)
    elif k * k > n:
        print(n)
    else:
        f4(n, k + 1)

n = int(input())
f4(n)
