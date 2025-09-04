# for num in range(1, 100):
#     if num % 2 == 1:
#         print(num)

# Bonus question:
# for num in range(1, 100, 2):
#     print(num)

# Further exploration:
def print_odd_numbers():
    
    print('--> Welcome to the Print Consecutive Odd Numbers program!')
    start_value = int(input(
                  '--> Please enter your starting odd number value: '))
    end_value = int(input(
                '--> Please enter your ending odd number value: ')) + 1

    for num in range(start_value, end_value, 2):
        print(num)

print_odd_numbers() 
