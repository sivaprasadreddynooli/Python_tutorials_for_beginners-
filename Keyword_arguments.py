
def dumb_Sentence(name='siva',action='ate',item='mango'):
    print(name,action,item)

#we can send appropriate values in the order
dumb_Sentence('siva','ran','quickly')
#this will take the default values
dumb_Sentence()
#we should specify the argument values if not all values are passed
dumb_Sentence(action='skid',item='dangerously')
#we can send the values in the inorder
dumb_Sentence(item='apple',name='ravi')