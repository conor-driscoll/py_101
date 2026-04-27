num1 = 42
num2 = 100
num3 = 101

def between_10_and_100_inclusive(test_number):
    if 10 <= test_number <= 100:
        print(True)
    else:
        print(False)

between_10_and_100_inclusive(num1)
between_10_and_100_inclusive(num2)
between_10_and_100_inclusive(num3)

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))