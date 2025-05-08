# This code will print the following: 5
# This is because the values of variables defined at the global scope may be 
# accessed within functions.

num = 5

def my_func():
    print(num)

my_func()