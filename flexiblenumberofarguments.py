#the below function takes multiple arguments when we are not sure about number of arguments
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 34, 86)
add_numbers(3, 43, 54, 789, 123)

#the function name may be anything
def print_strings(*siva):
    for i in siva:
        print(i)

print_strings('ram', 'ravi', 'tej')
