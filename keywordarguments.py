def dumb_sentence(name='Siva',action='ate',item='tuna'):
    print(name,action,item)

#in below call default values will be taken when the function is called
dumb_sentence()
#in below call the given values will be called
dumb_sentence('ravi','runs','fast')
#only one item is passed , remaing default values will ne taken
dumb_sentence(item='sweet')
#we can pass in iregular order
dumb_sentence(item='rice',action='cooked')
