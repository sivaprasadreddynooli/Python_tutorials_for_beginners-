numberstaken = [12,13,14,15,16]

print("below are the numbers not taken")

# the use of continue statement
#whenever the continue statement is executed, it will stop executing the code present inside the code and
#will start from next iteration
for x in range(21):
    if x in numberstaken:
        continue
    print(x)
