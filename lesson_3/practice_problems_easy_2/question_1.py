numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reversed_numbers = []
for number in reversed(numbers):
    reversed_numbers.append(number)
print(reversed_numbers) 

print(numbers[::-1])

print(list(reversed(numbers)))