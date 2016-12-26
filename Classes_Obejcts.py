#always start class names with capital letter , its a good practice
#class is an easy way to group the similar types of functions and variables
class Enemy:
    life = 3
    #when we create the function in class , it autometically will create the self in the argumemt
    #that saying that it takes the values from the class itself
    #it means,give something from the same class

    def attack(self):
        print("ouch")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print("you are dead")
        else:
            print(self.life,"life left")

#to access any function present in side the class,we should create the objects of that class
#each object we create is an copy of its class
enemy1 = Enemy()
enemy2 = Enemy()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()