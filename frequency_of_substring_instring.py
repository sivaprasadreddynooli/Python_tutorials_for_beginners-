s = input()
ss = input()
count = 0
for i in range(len(s)):
    if s[i:(i+len(ss))] == ss:
        count = count + 1

print(count)