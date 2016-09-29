def add(args):
    return sum(args)

def subtract(args):
    return reduce(lambda x,y: x-y, args)

def multiply(args):
    return reduce(lambda x,y: x*y, args)

def divide(args):
    # Need to turn at least argument to float for division to
    # not be integer division
    floats = map(float, args)
    return reduce(lambda x,y: x/y, floats)

def square(args):
    # Needs only one argument
    return args[0] * args[0]


def cube(args):
    # Needs only one argument
    return args[0] * args[0] * args[0]

def power(args):

    return args[0] ** args[1]  # ** = exponent operator


def mod(args):
    return args[0] % args[1]
