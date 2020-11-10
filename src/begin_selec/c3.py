import sys

n = int(input())

tp = 0
xp = 0
yp = 0

for i in range(n):
    t, x, y = map(int, input().split())
    tr = abs(t - tp)
    xr = abs(x - xp)
    yr = abs(y - yp)
    
    if (tr - xr - yr) % 2 or tr < (xr + yr):
        print("No")
        sys.exit()

    tp = t
    xp = x
    yp = y

print("Yes")

