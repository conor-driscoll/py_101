def multisum(number):
    selected_multiples = set()

    for multiple in range(3, number + 1, 3):
        selected_multiples.add(multiple)

    for multiple in range(5, number + 1, 5):
        selected_multiples.add(multiple)

    return sum(selected_multiples)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)