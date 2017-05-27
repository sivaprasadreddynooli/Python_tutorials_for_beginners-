print(zip([1,2,3,4,5,6],'Hacker'))
#this will print - [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
print(zip([1,2,3,4,5,6],[1,2,3,4,5,6,7,8,9]))
#this will print [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
a = [1,2,3]
b = [6,5,4]
c = [7,8,9]
x = [a] + [b] + [c]
print(x)

print(zip(*x))
#this will print [(1, 6, 7), (2, 5, 8), (3, 4, 9)]