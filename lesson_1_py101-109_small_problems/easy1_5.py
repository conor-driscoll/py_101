print('--> Welcome to the tip calculator!')

bill = float(input('--> Please enter the bill amount using only digits '
                   'and at most one period: '))
tip_percentage = float(input('--> Please enter the tip percentage using only '
                             'digits and at most one period: '))

bill_multiplier = tip_percentage / 100
tip = bill_multiplier * bill
total = tip + bill

print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')