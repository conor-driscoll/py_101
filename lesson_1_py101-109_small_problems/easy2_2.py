name = input('--> What is your name? ')

if '!' not in name:
    print(f'--> Hello {name}.')
else:
    print(f'--> HELLO {name.upper()}! WHY ARE WE YELLING?')