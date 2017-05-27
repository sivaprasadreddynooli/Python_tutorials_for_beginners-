a = int(input())
x = list(input().split())
x = [int(y) for y in x]
s = set(x)
res = 0
print(x)
#n = (len(x) - 1)//a
for q in s:
    if 1 == x.count(q):
        print(q)
        break
    res = q



'''
print(x)
for t in x:
    res = res^t
print(res)

a = int(input())
x = input()
x = x.replace(' ','')
s = set(x)
q = set(s)
for y in s:
    if x.count(y) != 1 :
        q.remove(y)
for t in q:
    print(t)


'''