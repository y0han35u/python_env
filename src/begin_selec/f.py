n, a, b = map(int, input().split())
cnt = 0
li = list(range(n + 1))

for i in li:
    l = [int(x) for x in list(str(i))]
    s = 0
    for j in l:
        s += j
    if s >= a and s <= b:
        cnt += i
print(cnt)
