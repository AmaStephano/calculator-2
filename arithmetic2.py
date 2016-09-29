def add(args):
    return sum(args)

def subtract(args):
    # use anonymous (lamdba) function and pass in list of args to be
    # able to run on infinite amount of args
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
    # ** = exponent operator
    return args[0] ** args[1]  

def mod(args):
    return args[0] % args[1]

def my_reduce(func, some_list):
    total = some_list[0]
    for num in some_list[1:]:
        total = func(total, num)
    return total