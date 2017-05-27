a = list(map(int,input().split()))
tpl = []
for _ in range(a[0]):
    b = list(map(int,input().split()))
    tpl = [b] + tpl
k = int(input())
#this is the way to sort the  nested lists on a key value
final = tpl.sort(key=lambda x: int(x[k]))
#the below statement will print values in a single line without brackets
for i in tpl:
        print(*i)
#print(zip(*tpl)

'''
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
'''

