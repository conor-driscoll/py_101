def multiply(factor1, factor2):
    return factor1 * factor2

# def square(number):
#     return multiply(number, number)

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True


# Further exploration:
def power_to_the_n(number, exponent):
    current_number = 1
    
    for _ in range(exponent):
        current_number = multiply(number, current_number)

    return current_number


print(power_to_the_n(5, 2) == 25)
print(power_to_the_n(1, 10) == 1)
print(power_to_the_n(0, 4) == 0)
print(power_to_the_n(4, 0) == 1)