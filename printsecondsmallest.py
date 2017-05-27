n = int(input())
c = []
d = []
x = 100
y = 100
z = ''
for i in range (0,n):
    a = input()
    b = float(input())
    c.append(a)
    c.append(b)
    d.append(c)
    c = []
sorted(d)
x = d[0][1]
l = []
print(x)
print(len(d))
for i in range(1,len(d)):
    if x < d[i][1] and l == []:
        l.append(d[i][0])
        x = d[i][1]
        continue
    if x == d[i][1] and l == []:
        continue
    if x == d[i][1] and l != []:
        l.append(d[i][0])
    if x < d[i][1] and l != []:
        break

for i in range(0,len(l)):
    print(i)