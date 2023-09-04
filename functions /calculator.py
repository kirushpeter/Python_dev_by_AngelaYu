 
# function to add

def add(n1, n2):

    return n1 + n2

# function to subtract

def subtract(n1, n2):

    return n1 - n2


# function to multiply

def multiply(n1, n2):

    return n1 * n2


# function to divide

def divide(n1, n2):

    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    num1 = float(input("What is the first number: "))

    for symbol in operations:

        print(symbol)


    should_continiue = True


    while should_continiue:


        operation_symbol = input("pick an operation from line above: ")

        num2 = float(input("What is the second number: "))

        calculation_function = operations[operation_symbol]


        answer = calculation_function(num1, num2) 
        
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        

        if input(f"Type 'Y' to continue calculating with {answer}, or type n to exit") == "y":

            num1 = answer

        else:

            should_continiue = False 

            calculator()   



calculator()






   



