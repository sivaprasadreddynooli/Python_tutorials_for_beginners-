#the below function defination states that the default value for the variable is unknown
#when no value is passed to the variable 'sex'
def get_gender(sex='unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex) 


get_gender("m")
get_gender("f")
#the below function takes unknown in the function
get_gender()