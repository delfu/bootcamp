# dont touch this function, it's for verifying tests
def expect_equal(a, b):
    if a != b:
        raise Exception("Wrong result", a, b)

def fib(x):
    # implement your function
    return 0

def fact(x):
    # implement your function
    return 0

def test():
    # feel free to modify this function to suit your needs but you'll need
    # to keep these tests
    for x in range(1000000):
        result_1 = fib(x)
        expect_equal(result_1, fib(x - 1) + fib(x - 2))
        result_2 = fact(x)
        expect_equal(result_2, x * fact(x - 1))

test()