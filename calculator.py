"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


    # This is a program that runs until we press q
    # Initialize input string variable asks enter equation 
    # Initialize variable tokens as the tokenized version of input string
    # Develop conditionals for each function
    
while True:
    input_string = input("Enter equation:  ")
    tokens = input_string.split(' ')
    print (tokens)
    break