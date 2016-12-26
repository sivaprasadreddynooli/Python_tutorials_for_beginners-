#inheriting from more than one class
class Mario():

    def move(self):
        print("i am moving")

class Shroom():

    def eat_shroom(self):
        print("i am eating mushroom")

#we can inherit multiple classes
class Big_mushroom(Shroom,Mario):
    #you give pass , when you do not want to write any additional functionality
    #otherthan the inherited functions
    pass



bm = Big_mushroom()
bm.move()
bm.eat_shroom()