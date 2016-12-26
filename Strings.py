#strings should always be included inside the double quote("") or single quotes('')
print("i am siva reddy")
print('this is in single quote')
#the below sentence will give error
#the reason being it is confused , where to start as a string
#print('i don't think i am studied')
#so include double and single quote seperately , so that it can understand
print("i don't think i am studied");
#below statement works correctly , as it can understand things seperatelty
print('kalam said,"to work hard"')
#or else use"\t" to make it understand, which is called as escaping
print('i don\'t think i am studied')
#the below expression willnot print in sinle line , as it encounters a expression \n
print('c:\sivap\desktop\newpython')
#to print completely use r in the front fo the string
print(r'c:\sivap\desktop\newpython')
#assign strings to a variable
firstname = 'siva '
#print the value
print(firstname)
#assign second variable
lastname = 'nooli'
#we can concanate variables by + symbol
fullname = firstname + lastname
#print the full name
print(fullname)
#we can print same string multiple times by * symbol, the below expression prints firstname five times
print(firstname * 5)


