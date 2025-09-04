CURRENT_YEAR = 2025

current_age = int(input('\nWhat is your age? '))
retirement_age = int(input('At what age would you like to retire? '))

work_years_remaining = retirement_age - current_age
retirement_year = CURRENT_YEAR + work_years_remaining


print(f"\nIt's {CURRENT_YEAR}. You will retire in {retirement_year}.")
print(f"You have only {work_years_remaining} years of work to go!\n")