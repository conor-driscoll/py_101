def negative(number):
    if abs(number) != number:
        return number
    else:
        return number * -1


print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True