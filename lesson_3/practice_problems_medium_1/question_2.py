def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result


print(factors(10))
print(factors(80))

# Bonus question answer:
# number % divisor == 0 will be true if the divisor divides the number into an
# even dividend, or more concisely, if the divisor is a factor of the number.