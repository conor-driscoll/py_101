# Obtain two numbers from user input and assign to variables
# Obtain operator from user input and assign to a variable
# Place number variables on either side of the operator
# Print the result of this calculation


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

def prompt_test_num(message):
    num = input((f"==> {message}"))
    while True:
        try:
            int(num)
        except ValueError:
            num = input("==> Hmm... That doesn't look like a valid number.\n"
                        "==> Please re-enter\n")
            continue

        return int(num)

def prompt_test_opratr(message):
    opratr = input((f"==> {message}"))

    if number2 == 0 and opratr == "4":
        while opratr not in ["1", "2", "3"]:
            opratr = input("==> You must choose 1, 2, or 3 in this case, "
                           "since division by 0 is undefined.\n"
                           "==> Please re-enter\n")
    else:
        while opratr not in ["1", "2", "3", "4"]:
            opratr = input("==> You must choose 1, 2, 3, or 4.\n"
                           "==> Please re-enter\n")

    return int(opratr)


number1 = prompt_test_num("Welcome to the calculator\n"
                          "==> What's the first number? (digits only)\n")
number2 = prompt_test_num("What's the second number? (digits only)\n")
operation = prompt_test_opratr('What operation would you like to perform?\n'
                        '==> 1) Add, 2) Subtract, 3) Multiply, 4) Divide\n')


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