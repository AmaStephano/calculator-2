def add(args):
    return sum(args)

def subtract(args):
    total = args[0]
    for num in args[1:]:
        total -= num
    return total


def multiply(args):
    total = args[0]
    for num in args[1:]:
        total *= num
    return total


def divide(args):
    # Need to turn at least argument to float for division to
    # not be integer division
    floats = map(float, args)
    total = floats[0]
    for num in floats[1:]:
        total /= num
    return total


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
