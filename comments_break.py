magicnumber = 15
print('siva'+' nooli')
#+ is only , when adding two things of same data type
#below statement will give error
#print('siva' + 9)

#when concaninating two different data types use comma(,# )
print(9,'reddy')
print('vara','lakshmi')
print(24,56,67)
print(34+46)
#this is single line comment

for m in range(25):
    if m is magicnumber:
        print("the magic number is %s",m)
        #break the loop when the number is found and comeout of the loop
        break
    else:
        print(m)

'''
this is the multi line comment
for i in range(50):
    if i is magicnumber:
        print('magic number found')
'''