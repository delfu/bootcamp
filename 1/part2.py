# put your tests here, the first few are provided for you
tests = [
    "2 4 * 6 +",
    "25 4 * 1000 -"
]

import operator

operations = {
    "+": operator.add,
    "/": operator.truediv,
    "*": operator.mul,
    "-": operator.sub,
}

def validate_input(arguments):
    for arg in arguments:
        if arg not in operations:
            try:
                number = int(arg)
            except ValueError:
                return False
    return True
    

def your_function(test_string):
    arguments = test_string.split(" ")

    # this part is optional
    # the input of test_string here would be a valid sequence of operation. For assignment purposes, we'd skip validation
    # but to show you how to do it:
    if not validate_input(arguments):
        print("Error in test case: " + test_string)

    # a stack is just an array where we put values into it and remove from the end of it as we need
    # at the end, there should only be a single value and it's the result
    stack = []
    for arg in arguments:
        # we only evaluate when we see an operation
        if arg in operations:
            if len(stack) >= 2:
                # pop just removes the last item and puts in the variable
                # order is important because for operations like / or -
                b = stack.pop()
                a = stack.pop()
                # we evaluate the operation, and put the result at the end of the stack.
                # in the case of this assignment, there will never be more than 2 values on 
                # the stack because we are immediately evaluating the operation. But
                # if we were to support parentheses, a stack will have >2 values on it.
                stack.append(operations[arg](a, b))
            else:
                print("Error in test case: " + test_string)
                return None
        # if it wasnt an operation, we just add the value to the stack
        else:
            stack.append(int(arg))
    if len(stack) != 1:
        print("Error in test case: " + test_string)
        return None
    return stack.pop()

    # put your code here!
    return #return will let you pass some value back to the caller of this function, in this case it doesnt really matter

for test in tests:
    print(your_function(test))