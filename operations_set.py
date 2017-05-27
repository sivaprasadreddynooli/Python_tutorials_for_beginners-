#declare a set with below statement ,not wirh  {}, which declares emptly dictionary
a = set()
b = {1,2,567,454,}
a.add(1)
a.add(1234)
a.add(23)

print(len(a))

a.update(b)
print(a)

#removes if present , if not will show keyerror
a.remove(23)
#just tries to remove the element
a.discard(99)
print(a)
#removes random element
a.pop()
print(a)
#the below statement will clear the set
a.clear()
#we also have set functions - union() , intersection(),difference(),
print(a)