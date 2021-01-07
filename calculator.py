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
    
    
while True:
    input_string = input("Enter equation:  ")
    tokens = input_string.split(' ')
    
    if input_string == 'q':
        break
    if tokens[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))