# import json
# # Open the JSON file for reading
# with open('calculator_messages.json', 'r') as file:
#     MESSAGES = json.load(file)
# Now 'MESSAGES' contains the contents of the JSON file as a Python dictionary
# or list

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

import os

MESSAGES = {
"english" : {
    "prompt_test_operator_message1" : 
    "==> You must choose 1, 2, or 3 in this case, since division by 0 is "
    "undefined.\n==> Please re-enter\n",
    "prompt_test_operator_message2" : 
    "==> You must choose 1, 2, 3, or 4.\n==> Please re-enter\n",
    "welcome_message":
    "==> Welcome to the calculator!\n",
    "number1_message" : 
    "What's the first number?\n\n",
    "number2_message" : 
    "What's the second number?\n\n",
    "operation_message" : 
    "Please enter an operation code.\n\n==> 1) Add, 2) Subtract, 3) Multiply, "
    "4) Divide\n\n",
    "another_calculation_message" : 
    "==> Please enter 'yes' to perform another calculation or 'no' to exit "
    "the program.\n\n",
    "invalid_entry_message" :
    "==> Invalid entry received:",
    "decimal_answer_message" :
    "(value has been rounded to two decimal places)\n",
    "goodbye_message" :
    "==> Goodbye until next time!\n",
            },
"espanol" : {
    "prompt_test_operator_message1" :
    "==> Debes elegir 1, 2 o 3 en este caso, ya que la división por 0 no "
    "está definida.\n==> Por favor vuelve a entrar\n",
    "prompt_test_operator_message2" :
    "==> Debes elegir 1, 2, 3 o 4.\n==> Por favor vuelve a entrar\n",
    "welcome_message":
    "==> ¡Bienvenido a la calculadora!\n",
    "number1_message" :
    "¿Cuál es el primer número?\n\n",
    "number2_message" :
    "¿Cuál es el segundo número?\n\n",
    "operation_message" :
    "Por favor, introduzca un código de operación.\n\n==> 1) Sumar, 2) "
    "Restar, 3) Multiplicar, 4) Dividir\n\n",
    "another_calculation_message" :
    "==> Ingrese 'sí' para realizar otro cálculo o 'no' para salir del "
    "programa.\n\n",
    "invalid_entry_message" :
    "==> Entrada no válida recibida:",
    "decimal_answer_message" :
    "(el valor se ha redondeado a dos decimales)\n",
    "goodbye_message" :
    "==> Adiós, amigo!\n",
            },
}

def language_selector():
    os.system('clear')
    while True:
        language_input = input("==> Please enter 'English' for calculator "
                               "program messages in English.\n"
                               "==> Por favor, introduzca 'Español' para los "
                               "mensajes del programa de la calculadora "
                               "en Español.\n\n")

        language_function = language_input.lower()

        if language_function == 'español':
            language_function = 'espanol'

        match language_function:
            case 'english' | 'espanol' :
                os.system('clear')
                return language_function
            case _ :
                os.system('clear')
                print(f"==> Invalid entry received: {language_input}\n"
                      f"==> Entrada no válida recibida: {language_input}\n")

def prompt_test_number(message):
    while True:
        number = input((f"==> {message}"))
        try:
            os.system('clear')
            return int(number)
        except ValueError:
            try:
                os.system('clear')
                return float(number)
            except ValueError:
                os.system('clear')
                print(f'{MESSAGES[LANGUAGE]["invalid_entry_message"]} '
                      f'{number}\n')

def prompt_test_operator(message, number2_argument):
    operator = input((f"==> {message}"))

    if number2_argument == 0 and operator == "4":
        while operator not in ["1", "2", "3"]:
            os.system('clear')
            operator = input(f'{MESSAGES[LANGUAGE]["invalid_entry_message"]} '
                             f'{operator}\n\n'
                    f'{MESSAGES[LANGUAGE]["prompt_test_operator_message1"]}\n')
    else:
        while operator not in ["1", "2", "3", "4"]:
            os.system('clear')
            operator = input(f'{MESSAGES[LANGUAGE]["invalid_entry_message"]} '
                             f'{operator}\n\n'
                    f'{MESSAGES[LANGUAGE]["prompt_test_operator_message2"]}\n')

    os.system('clear')
    return int(operator)

def calculator(operation_argument, number1_argument, number2_argument):
    match operation_argument:
        case 1:
            return number1_argument + number2_argument, '+'
        case 2:
            return number1_argument - number2_argument, '-'
        case 3:
            return number1_argument * number2_argument, 'x'
        case 4:
            return number1_argument / number2_argument, '/'

def another_calculation_prompt():
    while True:
        another_calculation_input = input(MESSAGES[LANGUAGE]
                                    ["another_calculation_message"])
        another_calculation_function = another_calculation_input.lower()

        os.system('clear')

        match another_calculation_function:
            case 'no':
                print(MESSAGES[LANGUAGE]["goodbye_message"])
                return another_calculation_function
            case 'yes' | 'sí' | 'si' :
                return another_calculation_function
            case _ :
                os.system('clear')
                print(f'{MESSAGES[LANGUAGE]["invalid_entry_message"]}',
                      another_calculation_input)


LANGUAGE = language_selector()

print(MESSAGES[LANGUAGE]["welcome_message"])

while True:
    number1 = prompt_test_number(MESSAGES[LANGUAGE]["number1_message"])
    number2 = prompt_test_number(MESSAGES[LANGUAGE]["number2_message"])
    operation = prompt_test_operator(MESSAGES[LANGUAGE]["operation_message"],
                                     number2)
    output, operation_symbol = calculator(operation, number1, number2)

    if isinstance(output, float):
        print(f'{number1} {operation_symbol} {number2} = {output:,.2f} '
              f'{MESSAGES[LANGUAGE]["decimal_answer_message"]}')
    else:
        print(f"{number1} {operation_symbol} {number2} = {output:,}\n")

    another_calculation = another_calculation_prompt()
    if another_calculation == 'no':
        break