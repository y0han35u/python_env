n = int(input())
li = sorted([int(x) for x in input().split()], reverse=True)

even_li = [i for i in range(0, n, 2)]
alice = 0

for j in even_li:
    alice += li[j]

bob = sum(li) - alice

print(alice - bob)




