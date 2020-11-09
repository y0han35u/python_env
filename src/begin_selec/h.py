n = int(input())
li = [int(input()) for _ in range(n)]

li_unq = list(set(li))

print(len(li_unq))
