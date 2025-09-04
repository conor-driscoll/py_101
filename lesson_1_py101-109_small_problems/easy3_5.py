def triangle(n):
    for i in range(1, n + 1):
        space_number = n - i
        print((space_number * ' ') + (i * '*'))

triangle(5)
triangle(9)