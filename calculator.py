"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *

raw_file = open("calcinput.txt")
output = open("output.txt", "a")

# Your code goes here
#loop forever

    # get input

for line in raw_file:

    tokens = line.strip().split(" ")
    if tokens[0] != "q" and len(tokens) < 2:
        print "You didn't enter enough arguments."
        continue 

    # use map function to turn items 1 and beyond in a list into ints
    # perform int function on all items in tokens from index 1 on
    try:
        args = map(int, tokens[1:])
    except ValueError:
        print "You entered an invalid input"
        continue

    #if "q". quit out of program
    
    if tokens[0] == "+":
        output.write("%.2f\n" % add(args))

    elif tokens[0] == "-":
        output.write("%.2f\n" % subtract(args))

    elif tokens[0] == "*":
        output.write("%.2f\n" % multiply(args))

    elif tokens[0] == "/":
        output.write("%.2f\n" % divide(args))

    elif tokens[0] == "square":
        output.write("%.2f\n" % square(args))

    elif tokens[0] == "cube":
        output.write("%.2f\n" % cube(args))
        
    elif tokens[0] == "pow":
        output.write("%.2f\n" % power(args))

    elif tokens[0] == "mod":
        output.write("%.2f\n" % mod(args))
    
    else:
        print "You entered an invalid command"
      

raw_file.close()