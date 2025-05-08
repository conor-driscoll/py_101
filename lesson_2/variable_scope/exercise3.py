# This code will print the following: 10
# Due to the global keyword being used on line 4, it is the global num variable
# which is reassigned on line 5. As a result, it is this new, reassigned value
# which is passed into the print function on line 8.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)