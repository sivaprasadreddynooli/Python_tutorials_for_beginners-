#inport the module name , from whom you are expecting to use the functions
import module1
import random

#we have the specify the module name , the reason being we import multiple modules, there may be chances that
#modules a have defined a function with same name in so many modules, so specify the module name before the function
module1.fish()

x = random.randrange(1,1000)
print(x)