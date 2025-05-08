# This code will print the following: 5
# This is because the num variable being shadowed within my_func, does nothing
# to change its value at the global scale. Therefore, when num is passed into
# the print function on line 7, the value accessed will be unchanged from 
# when it was defined on line 1.

num = 5

def my_func():
    num = 10

my_func()
print(num)