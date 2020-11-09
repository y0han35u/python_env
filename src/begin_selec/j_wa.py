#this is wrong answer
n, yen = map(int, input().split())

xr = yen % 10000
yr = xr % 5000
zr = xr % 1000
zr2 = yr % 1000

x = int(yen / 10000)
y = int(xr / 5000)
z = int(xr / 1000)
z2 = int(yr /1000)

if xr == 0 and n == x:
    print(x, 0, 0)
elif yr == 0 and n == x + y:
    print(x, y, 0)
elif zr == 0 and n == x + z:
    print(x, 0, z)
elif zr2 == 0 and n == x + y + z2:
    print(x, y, z)
else:
    print("-1 -1 -1")


