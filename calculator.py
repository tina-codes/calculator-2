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

    #while != q:

        input_string = input("Please enter your equation > ")

        if input_string == "q":
            break

        else:
            token = input_string.split(" ")

            #print(" Select [+] if you wold like to add")

            arithmetic_function = token[0]
            num1 = int(token[1])
            num2 = int(token[2])
        
            if arithmetic_function == "+":
                sum = add(num1, num2)
                print(sum)

            elif arithmetic_function == "-":
                sub = (subtract(num1, num2))
                print(sub)

use_calculator()
