
s = input()
l =[]
for x in range(len(s)):
    if s[x].upper():
       s[x].lower()
    elif s[x].lower():
       s[x].upper()
    else:
        s[x]
print(s)