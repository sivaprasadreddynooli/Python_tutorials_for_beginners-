# the function __init__ is inbuilt and comes everytime,  we create the objcet . we no need to call explicitely
class tuna():

    #the function will be called as soon as we create the object and the code in it will be executed first
    def __init__(self):
        print("this is init print statement from the init function")

    def swim(self):
        print("I am swimming")

#when we execute the statement the function will be called automatically
flipper = tuna()
flipper.swim()


#below class helps in demonistrating the init function by passing the parameter to it
#that will be executed when ever the object is created
class Enemy():

    def __init__(self,x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()



