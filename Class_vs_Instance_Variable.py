
class Girl:

    #this is a class variable , same for every object created from the class
    gender = 'female'

    #name here is a instance variable and varies with the object created and mostly unique
    def __init__(self,name):
        self.name = name

r = Girl('ruchi')
s = Girl('sheebani')
print(r.gender)
print(s.name)
print(s.gender)
print(r.name)