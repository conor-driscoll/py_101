print('--> Welcome to the room square footage calculator!')

# length = float(input('--> Please enter the room length in meters: '))
# width = float(input('--> Please enter the room width in meters: '))

# square_footage_m2 = length * width
# square_footage_ft2 = square_footage_m2 * 10.7639  # square feet/square meter

# print(f'The room is {square_footage_m2:.2f} square meters or '
#       f'{square_footage_ft2:.2f} square feet.')


# Further exploration:
measurement_unit = input('--> Please enter "m" to enter measurements in '
                         'meters or enter any other value to enter in feet: ')

length = float(input('--> Please enter the room length: '))
width = float(input('--> Please enter the room width: '))

if measurement_unit == 'm':
    square_footage_m2 = length * width
    square_footage_ft2 = square_footage_m2 * 10.7639 # square ft/square m

    print(f'The room is {square_footage_m2:.2f} square meters '
          f'({square_footage_ft2:.2f} square feet).')

else:
    square_footage_ft2 = length * width
    square_footage_m2 = square_footage_ft2 / 10.7639  # square ft/square m

    print(f'The room is {square_footage_ft2:.2f} square feet '
          f'({square_footage_m2:.2f} square meters).')