#sometimes , we should break the functionality and work on small things congurrently - we need threading
#sometimes , we may not need threading , like calculations ,which produce unexpected results
import threading



class SivasMessenger(threading.Thread):
    #whenever we create the thread , it will call this run function
    def run(self):
        #when we donot care about the variable , but what to loop 10 times
        #we will give blank in the variable name
        for _ in range(10):
            print(threading.currentThread().getName())


#we can give a default name to every thread created
x = SivasMessenger(name='Send out the message')
y = SivasMessenger(name='Receive the messages')
#whenever we created a thread , we should call the function start  , it goes to the class and looks for the function run

#with threads , we no need to wait for the other thread to complete , the two threads work on the same time
x.start()
y.start()