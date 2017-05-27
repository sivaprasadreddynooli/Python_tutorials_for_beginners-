a = input()
b = input()
c = input()
d = input()
a = a.split()
b = b.split()
c = c.split()
d = d.split()
n = int(a[0])
m = int(a[1])
totalset = list(map(int,b))
c = list(map(int,c))
d = list(map(int,d))
seta = set(c)
setb = set(d)
print(totalset)
print(seta)
print(setb)
happ = 0
for i in totalset:
    if i in seta:
        print('yes',i)
        happ = happ + 1
    elif i in setb:
        print('No',i)
        happ = happ -1

print(happ)
