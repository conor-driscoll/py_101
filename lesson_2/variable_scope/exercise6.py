# This code will print the following: Inner 1: 25
#                                     Inner 2: 15

# Since for the first print call, which occurs on line 6, the outer
# function value of the variable x (15) is being shadowed by a reassignment of
# x within inner_func1, so it's this inner function value of 25 which
# is accessed. However, within inner_func2 there is no
# reassignment/shadowing of x, so therefore, on line 9, it is the outer 
# my_func value of x (15) which is accessed within the call to print.

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()