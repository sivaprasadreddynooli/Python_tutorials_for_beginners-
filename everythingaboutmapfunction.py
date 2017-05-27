#map function will be of the form map(aFunction, aSequence)

items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i **2 )
print(squared)

def sqr(x):return x**2
output = list(map(sqr,items))
print(output)

output2 = list(map(lambda x:x**2,items))
print(output2)

def double(x):
    return X*2
def triple(x):
    return X*3
func = [double,triple]
for i in range(5):
    value = map(lambda x:x(i),func)
print(value)

def pow(x,y):
    return  x**y

xy = list(map(pow,[2,3,4],[10,11,12]))
print(xy)

m = [1,2,3]
n = [4,5,6]
new_taple = map(None,m,n)
print(new_taple)


#map()