n = int(input())
div = 0
for _ in range(n):
    x = input().split()
    try:
        a = int(x[0])
        b = int(x[1])
        div = a//b
        print(div)
    except ZeroDivisionError:
        print("Error Code:","integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)




#the fucntions , string.lower(), string.upper() - will help in converting the
#string to a value either capital or small letters