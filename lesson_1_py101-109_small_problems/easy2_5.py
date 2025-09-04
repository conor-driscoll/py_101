def display_calc():
    number1 = float(input('==> Enter the first number:\n'))
    number2 = float(input('==> Enter the second number:\n'))
    operation_list = ['+', '-', '*', '/', '//', '%', '**']
    
    for operation in operation_list:
        match operation:
            case '+':
                result = number1 + number2
            case '-':
                result = number1 - number2
            case '*':
                result = number1 * number2
            case '/':
                result = number1 / number2
            case '//':
                result = number1 // number2
            case '%':
                result = number1 % number2
            case '**':
                result = number1 ** number2
            
        print(f'==> {number1} {operation} {number2} = {result}')


display_calc()
