#the variable a cab be accessed from any where inside the
a = 235

def corn():
    #the variable b is local to the function and cannot be accessed outside the function
    b = 12456
    print(a)
    print(b)

def mango():
    print(a)
    #we cannot print the value of b here , as it is local to the above function
    #print(b)

corn()
mango()
