
N = int(input())
L = [1,2,3]
for _ in range(N):
    a = []
    a = input().split()
    if a[0] == 'insert':
        L.insert(int(a[1]), int(a[2]))
    elif a[0] == 'remove':
        L.remove(int(a[1]))
    elif a[0] == 'append':
        L.append(int(a[1]))
    elif a[0] == 'print':
        print(L)
    elif a[0] == 'sort':
        L.sort()
    elif a[0] == 'reverse':
        L.reverse()
    if a[0] == 'pop':
        L.pop(2)
        print(L)
