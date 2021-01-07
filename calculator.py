"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


    # This is a program that runs until we press q
    # Initialize input string variable asks enter equation 
    # Initialize variable tokens as the tokenized version of input string
    # Develop conditionals for each function:
    # If input_string is 'q', break
    # If tokens at index 0 is '+'
    # Call the add function passing in the arguments, integers of tokens[1],[2]
    # Else if tokens at index 0 is '-'
    # Call the subtract function passing in the aguments same as for add function
    # Otherwise if tokens at index 0 is '*'
    # Call the multiply function passing in the same arguments as add function

    
while True:
    input_string = input("Enter equation:  ")
    tokens = input_string.split(' ')
    
    if input_string == 'q':
        break
    if tokens[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))
                