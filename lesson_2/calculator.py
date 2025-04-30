import json
# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)
# Now 'data' contains the contents of the JSON file as a Python dictionary or list

# Obtain two numbers from user input and assign to variables
# Obtain operator from user input and assign to a variable
# Place number variables on either side of the operator
# Print the result of this calculation


# Alternative functional solutions:

# def calculator(num1, num2, opratr_num):
#     if opratr_num == 1:
#         operator = '+'
#     elif opratr_num == 2:
#         operator = '-'
#     elif opratr_num == 3:
#         operator = '*'
#     elif opratr_num == 4:
#         operator = '/'
#         if num2 == 0:
#             return 'ERROR - division by zero'
#     else:
#         return 'ERROR - invalid input'
#
#     return eval(f'{num1} {operator} {num2}')

# output = calculator(number1, number2, operation)

# if operation == 1:
#     output = number1 + number2
# elif operation == 2:
#     output = number1 - number2
# elif operation == 3:
#     output = number1 * number2
# elif operation == 4:
#     if number2 == 0:
#         output = 'ERROR - division by zero'
#     else:
#         output = number1 / number2
# else:
#     output = 'ERROR - invalid input'


def prompt_test_num(message):
    num = input((f"==> {message}"))
    while True:
        try:
            int(num)
        except ValueError:
            num = input(data["prompt_test_num_msg1"])
            continue

        return int(num)

def prompt_test_opratr(message):
    opratr = input((f"==> {message}"))

    if number2 == 0 and opratr == "4":
        while opratr not in ["1", "2", "3"]:
            opratr = input(data["prompt_test_opratr_msg1"])
    else:
        while opratr not in ["1", "2", "3", "4"]:
            opratr = input(data["prompt_test_opratr_msg2"])

    return int(opratr)

while True:
    number1 = prompt_test_num(data["number1_msg"])
    number2 = prompt_test_num(data["number2_msg"])
    operation = prompt_test_opratr(data["operation_msg"])

    match operation:
        case 1:
            output = number1 + number2
        case 2:
            output = number1 - number2
        case 3:
            output = number1 * number2
        case 4:
            output = number1 / number2

    print(f'==> The result is: {output}')

    while True:
        another_calc = input(data["another_calc_msg"])
        try:
            another_calc = another_calc.lower()
        except ValueError:
            continue
        else:
            match another_calc:
                case 'yes' | 'no':
                    break

    if another_calc == 'no':
        break