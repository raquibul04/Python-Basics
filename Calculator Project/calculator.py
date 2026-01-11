#I am about to start on a new project. It will be on building a calculator
cont_calc = True

def summation(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
sum1 = 0
first_num = int(input("What's the first number?: "))
while cont_calc:
    operation = input("Pick an operation: ")
    second_num = int(input("What's the next number?: "))

    if operation == '+':
        sum1 = summation(first_num, second_num)
    elif operation == '-':
        sum1 = subtraction(first_num,second_num)
    elif operation == '*':
        sum1 = multiplication(first_num, second_num)
    elif operation == '/':
        sum1 = division(first_num,second_num)
    else:
        print("Invalid character")
    first_num = sum1
    continue_calculation = input(f"Type 'y' to continue calculating with {sum1}, or type 'n' to start a new calculation:").lower()
    if continue_calculation == 'n':
        cont_calc = False

    print(sum1)