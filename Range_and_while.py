#we can also loop through the for loop without the lists thats using the range
for x in range(10):
    print(x)

print("below are y values")
#it starts at 11 and ends at 19
#we specified start and end of values
for y in range(11,20):
    print(y)

print("below are z values")
#want to increment the values by particular value
#this increments by value 5 starting at 10 and ends at 40
for z in range(10,40,5):
    print(z)


print("below is the while loop")
#below are whiles loops
name = "siva"
x = 2
while(x < 10):
    print(name)
    x += 1