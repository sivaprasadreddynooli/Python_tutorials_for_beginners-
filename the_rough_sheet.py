s = list("HackerRank.com presents 'Pythonist 2'.")
l = []
for x in range(len(s)):
    if s[x].isupper():
        l.append(s[x].lower())
    elif s[x].islower():
        l.append(s[x].upper())
    else:
        l.append(s[x])
    #return ''.join(l)
print(''.join(l))