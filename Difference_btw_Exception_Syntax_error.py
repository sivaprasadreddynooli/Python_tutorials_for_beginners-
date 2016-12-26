#the below two lines of code works if the input is integer, what if the input is characters like "adfdfd"
#it will show valueerror - which is exception , not a syntax error
#value error - is when user cannot convert to integer type
tuna = int(input("please a number \n"))
print(tuna)

while True:
    try:
        x = int(input("enter a number siva \n"))
        print(18/x)
        break
    #when the user enter anything other than the number
    except ValueError:
        print('enter the number not a string')
    #When the dividion by zero happens
    except ZeroDivisionError:
        print("Donot pick the zero")
    #When we are not sure about the exception occuring
    except:
        print("some error happened")
    #When some code has to be executed somehow, no matter what
    finally:
        print("loop completed")