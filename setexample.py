b = set()
sum = 0
x = 0
a = int(input())
for i in range(1,a+1):
    x = (int(input()))
    if x not in b:
        sum = sum + x
    b.add(x)
a = len(b)
result = sum/a
print(result)