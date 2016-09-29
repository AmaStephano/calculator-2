"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *

# Your code goes here
#loop forever
while True:
    # get input
    user_input = raw_input("> ") 

    # split input into list
    tokens = user_input.split(" ") 

    # use map function to turn items 1 and beyond in a list into ints
    # perform int function on all items in tokens from index 1 on
    args = map(int, tokens[1:])

    #if "q". quit out of program
    if tokens[0] == "q":
        break
    
    elif tokens[0] == "+":
        print add(args)

    elif tokens[0] == "-":
        print subtract(args)

    elif tokens[0] == "*":
        print multiply(args)

    elif tokens[0] == "/":
        print divide(args)

    elif tokens[0] == "square":
        print square(args)

    elif tokens[0] == "cube":
        print cube(args)
        
    elif tokens[0] == "pow":
        print power(args)

    elif tokens[0] == "mod":
        print mod(args)
