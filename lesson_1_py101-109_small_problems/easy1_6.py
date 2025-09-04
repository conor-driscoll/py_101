integer = int(input('--> Please enter an integer greater than 0: '))
operation_code = input('--> Enter "s" to compute the sum, or "p" to compute '
                       'the product: ')

operation = 'sum' if operation_code == 's' else 'product'

if operation == 'sum':
    current_sum = 0
    for number in range(1, integer + 1):
        current_sum += number
    result = current_sum

else:
    current_product = 1
    for number in range(1, integer + 1):
        current_product *= number
    result = current_product

print(f'\nThe {operation} of the integers between '
      f'1 and {integer} is {result}.')