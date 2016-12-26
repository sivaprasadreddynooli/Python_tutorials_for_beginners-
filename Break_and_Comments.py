magicnumber = 29

#this is the single line comment given by "#"

'''
this is
multi
line comment given by "''''''"
'''


#below statement will print the concatenated  string
print("siva" + "reddy")

#below statement will give error , as it tries to add number to a string
#print("siva" + 9)

# to print numver and string with one print statement, use "," between the values
print(9,"siva")
print("sivanooli",9)


#the use of break statement
#will come out of the loop once it executes the statement break present inside the loop
for n in range(101):
    if n is magicnumber:
        print(n,"magic number found")
        break
    else:
        print(n)
