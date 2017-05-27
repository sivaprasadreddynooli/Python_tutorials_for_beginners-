from collections import Counter

mylist = [1,3,4,5,6,1,2,4,7,5,2,3,5,6,7,2,4,5,6,2,3,1,8]
print(Counter(mylist))
lis = Counter(mylist).items()
print(lis)
print((Counter(mylist)).items())
print((Counter(mylist)).keys())
print((Counter(mylist)).values())


X = int(input())
a = list(input().split())
N = int(input())

acount = (Counter(a))
print(acount)
print(acount.items())
ava = acount.values()
ake = acount.keys()
tot = 0
for _ in range(N):
    b = list(input().split())
    if b[0] in ake and acount[b[0]] > 0:
        print(b[1])
        tot = tot + int(b[1])
        acount[b[0]] = acount[b[0]] - 1
print(acount)
print(tot)
#for _ in range(N):


