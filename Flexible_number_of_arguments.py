#its always common to name the flexivle parameter as *args , we can name it as any thing
#we can send as many parameters as we want through *args parameter, when we are not sure about
#number of parameters to be passed
#we can name *args as anythong ,likw *tuna ,* siva
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)


add_numbers(3)
add_numbers(3,432,56)
add_numbers(12,13,57,24,67,345,4646)

