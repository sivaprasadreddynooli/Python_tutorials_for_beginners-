#the strings in python takes first letter as zero index , like arrays
user  = "i am reddy"
#the below expression prints first letter
print(user[0])
print(user[3])
#below is the blank letter
print(user[4])
#print the values from the last, not -0 which is zero
print(user[-1])
#print second letter from the last
print(user[-2])
#we can slice the string to a desired length by giving positions
print(user[2:8])
#if we donot specify first positon, it takes from the srart
print(user[:7])
#if we donot specify second position, it takes till the end
print(user[3:])
#below expression takes whole expression
print(user[:])
# we can find length by below functions
print(len(user))
#we can use same for the values as well
print(len("i am siva"))

