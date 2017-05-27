#cube = lambda x: # complete the lambda function 

def fibonacci(n):
    l = []
    if n == 1:
        l= [0]
    if n == 2:
        l = [0,1]
    if n > 2:
        l = [0,1]
        for i in range(2,n):
            l.append(l[i-1] + l[i-2])
    return l
    # return a list of fibonacci numbers
def cube(x):
    return x**3

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))