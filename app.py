from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dict = {}
dict["+"] = add
dict["-"] = subtract
dict["*"] = multiply
dict["/"] = divide

def calculator():
    should_continue = True
    first_num = int(input("What is your first number?:  "))

    while should_continue:
        for key in dict:
            print(key)
        operator = input("Choose an operation: ")
        second_num = int(input("What is your next number?: "))
        result = dict[operator](first_num, second_num)
        print(f" {first_num} {operator} {second_num} = {result}")
        to_continue = input("Do you want to continue with the previous result ('y') or start new ('n') ?")
        if to_continue == 'y':
            first_num = result
        else:
            should_continue = False
            print("\n" * 100)
            calculator()


calculator()







