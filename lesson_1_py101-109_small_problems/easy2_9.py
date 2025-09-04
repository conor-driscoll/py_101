import random


# random_age = random.randrange(20, 101)
# print(f'Teddy is {random_age} years old!')


# Further exploration:
name = input('--> If you enter the name of an imaginary person, an age will '
             'be randomly generated for them.\n'
             '--> If you hit enter without typing anything, the imaginary '
             'person will be assigned the name "Teddy".\n'
             '--> Please enter: ')
if not name: # If the name string is empty
    name = 'Teddy'

random_age = random.randrange(20, 101)

print(f'--> {name} is {random_age} years old!')