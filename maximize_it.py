from itertools import product

k, m = [int(x) for x in input().split(' ')]
mlist = list()
sumlist = list()
for i in range(k):
    mlist.append([int(x) ** 2 for x in input().split()][1:])
print(mlist)
mlist = list(product(*mlist))
print(mlist)
for i in mlist:
    sumlist.append(sum(i) % m)

print(max(sumlist))

'''
input
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

'''