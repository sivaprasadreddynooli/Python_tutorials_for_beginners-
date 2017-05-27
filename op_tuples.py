scores = []
n, x = map(int, input().split())
for i in range(x):
    scores.append(list(map(float, input().split())))
print(scores)
print(*[sum(student)/len(student) for student in zip(*scores)],sep='\n')
