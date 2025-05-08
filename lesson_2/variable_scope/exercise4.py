# This code will print the following: Hello World
# This is because, for the print function invocation on line 6, the
# 'Hello' value of outer_var is accessible due to its location in an outer 
# function, and inner_var's value is accessible as it can be found in the 
# same inner function as the print invocation.

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()