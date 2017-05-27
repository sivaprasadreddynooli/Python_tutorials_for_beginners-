n = int(input())
a = set(list(input().split()))
m = int(input())
sum = 0
for _ in range(m):
    b = list(input().split())
    c = set(list(input().split()))
    if b[0] == 'intersection_update':
        a.intersection_update(c)

    elif b[0] == 'update':
        a.update(c)

    elif b[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(c)

    elif b[0] == 'difference_update':
        a.difference_update(c)
print(a)
s = list(a)
p = [int(x) for x in s]
l =sum(s)
print(p)
# sum = sum + int(x)  for x in a
#print(sum(Decimal(x) for x in s))
