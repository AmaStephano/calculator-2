"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *
 
# get input
input_file = open("calcinput.txt")

# create output file to append to
output = open("output.txt", "a")

for line in input_file:

    # strip spaces off the left and right ends & split on a " "
    tokens = line.strip().split(" ")

    # make sure they entered at least 2 items
    if tokens[0] != "q" and len(tokens) < 2:
        output.write("You didn't enter enough arguments.")
        continue 

    # use map function to turn items 1 and beyond in a list into ints
    # perform int function on all items in tokens from index 1 on
    try:
        args = map(int, tokens[1:])
    except ValueError:
        output.write("You entered an invalid input")
        continue
    
    if tokens[0] == "+":
        # %.2f limits output to 2 decimals
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
        output.write("You entered an invalid command")
      

input_file.close()
output.close()
