first= ['siva','ravi','bindu']
last = ['nooli','fake','mooli']

#zip will help in joining the lists
names = zip(first,last)

#its actually making the list of tuples like below
#[('siva','nooli'),('ravi','fake'),('bindu','mooli')]

for a,b in names:
    print(a,b)