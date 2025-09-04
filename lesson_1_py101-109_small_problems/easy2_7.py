def xor(argument1, argument2):
    if argument1 and argument2:
        return False
    
    return bool(argument1 or argument2)

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

# Further exploration:
# I completed the thought experiments