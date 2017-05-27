#lists and tuples can contain any type of elements, unlike strings , which handles only character type of strings
a = [1,2,56,343,34]
#the below operation allends the element to the list
a.append(233)

b = [12,4,897,378,34793]

a.extend(b)

a.insert(1,111)
#prints the position of the value
print(a.index(897))
a.remove(378)
a.pop()
print(a)
a.reverse()
print(a)
#sort the list
a.sort()
print(a)
a.sort(reverse=True)
print(a)