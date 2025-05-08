# Collect the APR and loan amount and duration from user input and convert to
# floats
# Built a monthly mortgage payment calculator, given the APR and the loan
# amount and duration
# Calculate monthly interest rate and loan duration in months
# Ensure that edge cases and bad input are accounted for
# Ensure that multiple calculations can be made
# Ensure that negative numbers are handled appropriately
# Ensure that no lines are too long

import os


def loan_amount_input():
    while True:
        loan_amount_function = input("==> Please enter a positive number for "
                                     "the total loan amount in dollars, using "
                                     "only digits and, at most, one period.\n")
        try:
            loan_amount_function = float(loan_amount_function)
        except ValueError:
            os.system('clear')
            print(f'==> Invalid entry received: {loan_amount_function}')
        else:
            if loan_amount_function <= 0:
                os.system('clear')
                print("==> Non-positive number received:",
                      loan_amount_function)
            else:
                return loan_amount_function

def apr_months_input():
    while True:
        apr_function = input("==> Please enter a non-negative number for the "
                             "Annual Percentage (interest) Rate (APR) of the "
                             "loan, using only digits and, at most, one "
                             "period.\n"
                             "==> For example, an entry of '0.50' will be "
                             "interpreted as an APR of 0.5%.\n")
        try:
            apr_month = (float(apr_function) / 100) / 12
        except ValueError:
            os.system('clear')
            print(f'==> Invalid entry received: {apr_function}')
        else:
            if apr_month < 0:
                os.system('clear')
                print(f'==> Negative number received: {apr_function}')
            else:
                return apr_function, apr_month

def loan_duration_months_input():
    while True:
        months_or_years = input("==> Please enter 'm' to enter the loan "
                             "duration in months or 'y' to enter in years.\n")
        match months_or_years:
            case 'm' | 'y' :
                break
            case _ :
                os.system('clear')
                print(f'==> Invalid entry received: {months_or_years}')

    os.system('clear')

    while True:
        if months_or_years == 'm':
            loan_duration_months_function = input(
            "==> Please enter a positive number for the total loan duration "
            "in months, using only digits and, at most, one period.\n")
            loan_duration_string_function = (loan_duration_months_function +
                                             ' months')
            try:
                loan_duration_months_function = float(
                                                loan_duration_months_function)
            except ValueError:
                os.system('clear')
                print('==> Invalid entry received:',
                      loan_duration_months_function)
            else:
                if loan_duration_months_function <= 0:
                    os.system('clear')
                    print("==> Non-positive number received:",
                          loan_duration_months_function)
                else:
                    return (loan_duration_string_function,
                            loan_duration_months_function)
        else:
            loan_duration_years = input("==> Please enter a positive number "
                                        "for the total loan duration in "
                                        "years, using only digits and, at "
                                        "most, one period.\n")
            loan_duration_string_function = loan_duration_years + ' years'
            try:
                loan_duration_months_function = ((float(loan_duration_years))
                                                 * 12)
            except ValueError:
                os.system('clear')
                print(f'==> Invalid entry received: {loan_duration_years}')
            else:
                if loan_duration_months_function <= 0:
                    os.system('clear')
                    print("==> Non-positive number received:",
                        loan_duration_years)
                else:
                    return (loan_duration_string_function,
                            loan_duration_months_function)

def monthly_payment_calculator(loan_amount_argument,
    monthly_interest_rate_argument, loan_duration_months_argument):
    if monthly_interest_rate_argument == 0:
        monthly_payment_function = (loan_amount_argument /
        loan_duration_months_argument)
    else:
        monthly_payment_function = (loan_amount_argument *
        (monthly_interest_rate_argument /
        (1 - (1 + monthly_interest_rate_argument) **
        -loan_duration_months_argument)))
    return monthly_payment_function


print('==> Welcome to the monthly loan payment calculator!')

while True:
    loan_amount = loan_amount_input()
    os.system('clear')
    apr, monthly_interest_rate = apr_months_input()
    os.system('clear')
    loan_duration_string, loan_duration_months = loan_duration_months_input()
    os.system('clear')

    monthly_payment = monthly_payment_calculator (loan_amount,
    monthly_interest_rate, loan_duration_months)

    print(f'==> For the following values...\n'
          f'Loan amount: ${loan_amount:,.2f}\n'
          f'APR: {apr}%\n'
          f'Loan duration: {loan_duration_string}\n'
          f'==> The monthly payment is: ${monthly_payment:,.2f}')

    while True:
        another_calculation = input("==> Would you like to calculate another "
                                    "loan payment?\n"
                                    "==> Please enter 'y' for yes or 'n' "
                                    "for no.\n")
        match another_calculation:
            case 'y' | 'n' :
                break
            case _ :
                os.system('clear')
                print(f'==> Invalid entry received: {another_calculation}')

    if another_calculation == 'n':
        break

    os.system('clear')