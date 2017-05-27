a = input().split()
N = int(a[0])
X = int(a[1])
tpl = []
for z in range(X):
    a = list(map(float,input().split()))
    tpl = [a] + tpl
for i in zip(*tpl):
    print(sum(i)/X)

'''
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
'''