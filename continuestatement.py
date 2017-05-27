numberstaken = [2,7,8,12,17]

print('the avilable numbers for jersey ')
for i in range(1,21):
    if i in numberstaken:
        #come out of the current iteration and start from the next number
        continue
    print(i)