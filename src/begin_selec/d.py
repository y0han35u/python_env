n = input()

li = [int(i) for i in input().split()]

cnt = 0

while 1:
    if any([i % 2 == 1 for i in li]):
        break
    cnt += 1
    li = [e / 2 for e in li]

print(cnt)

