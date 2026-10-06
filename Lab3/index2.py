A = int(input())
B = int(input())
mx = max(A, B)
mn = min(A, B)
if mn == A:
    print(list(range(mn, mx + 1)))
elif mn == B:
    print(list(range(mn, mx + 1))[::-1])
