#Map function applies to all the elements of the list
#applies a function to all the items in an input_list

#map(function_to_apply, list_of_inputs)


#the result from the map is always list

items = [2,3,4,5]

squares = []
for i in items:
    squares.append(i**2)
print(squares)

itm = [1,2,3,5,67,78,4]
sqr = list(map(lambda x:x**3,itm))
print(sqr)


#filter function- creates a list of elements for which a function returns true.
num_list = [-2,-4,-6,-81,3,5,6,7,1]
less_than_zero = list(filter(lambda x:x<0,num_list))
print(less_than_zero)

#reduce function
#its useful for performing some operation on a list and and returning the result
from functools import  reduce
product = reduce((lambda x,y:x*y),[1,2,3,4])
print(product)


#the function in map need not be lambda
items1 = [1,2,3,4,5,6,7,8]
def sqrr(x):
    return x**2
print(list(map(sqrr,items1)))

#the map can work on two functions at the same time
def square1(y):
    return y**2
def cube(y):
    return y**3

func = [square1,cube]
for r in range(5):
    print(list(map(lambda x:x(r),func)))



#the none function will produce tuple
m = [1,2,3]
n = [6,7,8]
tpl = (map(None, m, n))
print(tpl)