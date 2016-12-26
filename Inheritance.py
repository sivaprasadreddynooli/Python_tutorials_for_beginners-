#inheritance means getting something from someoneelse
class parent():

    def last_name(self):
        print("nooli")


#the class from which we are inheriting goes in to the class parameter
#the child will gets all of its classes from its inherited class
# it means , the child class will have two functions - last_name and fisrt_name
#the parent will have only one function
class child(parent):

    def first_name(self):
        print('siva reddy')
    #we can also override the functions of parent class
    def last_name(self):
        print("reddygari")

prasad = child()
prasad.first_name()
prasad.last_name()