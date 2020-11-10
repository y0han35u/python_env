import sys

n, yen = map(int, input().split())

for i in range(n + 1):
    for j in range(n + 1 - i):
        k = n - (i + j)
        if 10000 * i + 5000 * j + 1000 * k == yen:
            print(i, j, k)
            sys.exit()

print('-1 -1 -1')

