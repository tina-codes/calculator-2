"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
"""repeat forever:
    read input
    tokenize input
        if the first token is "q":
            quit
        else:
            (decide which math function to call based on first token)
            if the first token is 'pow':
                  call the power function with the other two tokens

            (...etc.)"""
def use_calculator():
    
    while True:

        input_string = input("Please enter your equation > ")

        if input_string == "q":
            break

        else:
            token = input_string.split(" ")

            arithmetic_function = token[0]
            num1 = float(token[1])
            num2 = float(token[2])
        
            if arithmetic_function == "+":
                solution = add(num1, num2)

            elif arithmetic_function == "-":
                solution = subtract(num1, num2)

            elif arithmetic_function == "*":
                solution = multiply(num1, num2)
                
            elif arithmetic_function == "/":
                solution = divide(num1, num2)

            elif arithmetic_function == "square":
                solution = square(num1, num2)
            
            elif arithmetic_function == "cube":
                solution = cube(num1, num2)
            
            elif arithmetic_function == "pow":
                solution = power(num1, num2)

            elif arithmetic_function == "mod":
                solution = mod(num1, num2)
        
        print("{:.2f}".format(solution))
           
use_calculator()
