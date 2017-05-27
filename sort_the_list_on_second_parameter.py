'''
students = []
for _ in range(int(input())):
    l = []
    name = input()
    score = float(input())
    l.append(name)
    l.append(score)
    students.append(l)
students.sort(key=lambda x: x[0])
students.sort(key=lambda x: x[1])
print(students[1][1], students[1][0])
'''
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

print(marksheet)
print(sorted(list(set([marks for name, marks in marksheet]))))
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]

print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))