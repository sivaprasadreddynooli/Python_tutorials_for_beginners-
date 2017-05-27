import numpy
a = list(input().split())
#input 1 2 3 4 5 6 7 8 9
array1 = numpy.array(a,float)
print(array1)
array2 =array1.reshape(3,3)
print(array2)

b = [1, 2, 3, 4, 5]
array3 = numpy.array(b)
print(array3.shape)
c = [[1, 2],[3, 4],[6,5]]
array4 = numpy.array(c)
print(array4.shape)