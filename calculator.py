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

#while calculating:
#string = "pow, num1, num2"

input_string = input("Please enter your calculation ")
     
token = input_string.split(" ")

arithmetic_function = token[0]
num1 = int(token[1])
num2 = int(token[2])
    
if arithmetic_function == "+":
    sum = add(num1, num2)
    print(sum)