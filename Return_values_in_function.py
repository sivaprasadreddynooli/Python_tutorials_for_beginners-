#this function will not print anything ,but returns the value to the called function
def allowed_Age(my_Age):
    girlsage = my_Age/2 + 7
    return girlsage


#here we are getting the returned values to the variables
siva_allowed_age = allowed_Age(25)
ravi_allowed_age = allowed_Age(29)
print("siva can date girls of age ",siva_allowed_age,"or older")
print("ravi can date girls of age ",ravi_allowed_age,"or older")