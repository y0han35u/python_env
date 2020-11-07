cnt = int(input())

pnt = [tuple(map(int, input().split())) for i in range(cnt)]

for i in range(cnt):
    if i < 2:
        continue
    for j in range(i):
        if j < 1:
            continue
        for k in range(j):
            x1, y1 = pnt[i]
            x2, y2 = pnt[j]
            x3, y3 = pnt[k]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x2 * y1 == x1 * y2:
                print('Yes')
                exit()

print('No')
