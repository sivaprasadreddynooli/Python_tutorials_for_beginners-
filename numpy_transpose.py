import numpy

a = numpy.array([[1,2,3],
                [4,5,6]])
print(numpy.shape(a))
print(numpy.transpose(a))
print(a.flatten())

a = list(map(int,input().split()))
l = []
for i in range(a[0]):
    d = list(map(int,input().split()))
    l.append(d)
print(l)
