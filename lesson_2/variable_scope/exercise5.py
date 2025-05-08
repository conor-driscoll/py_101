# This code will raise a NameError
# This is because num is passed into the print function at the global level on
# line 5, however, the num variable hasn't been defined at the global level.

def my_func():
    num = 10

my_func()
print(num)