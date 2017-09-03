#the idea of dictionary is that it has keys and values

classmates = {'siva':' is a good boy','ravi':' is a fake boy','satish':' he is so awesome'}
print(classmates['siva'])
print(classmates['ravi'])

print("below are the values by iteration")
#we can iterate through the loop in below way
for k,v in classmates.items():
    print(k + v)

print("this is all about the dictionary")