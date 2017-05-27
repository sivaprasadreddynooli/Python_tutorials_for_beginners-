string = 'AABCAAADA'
k = 3
# your code goes here
for i in range(0, len(string), k):
    a = list(string[i:(i + k)])
    for b in range(k-1):
        for c in range((b+1),k):
            if a[b] == a[c]:
                a[c] = ''
    a = ''.join(a)
    print(a)
#below code is the code found online
'''
s = input()
k = int(input())
num_subsegments = int(len(s) / k)

for index in range(num_subsegments):
    # Subsegment string
    t = s[index * k: (index + 1) * k]

    # Subsequence string having distinct characters
    u = ""

    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)
'''