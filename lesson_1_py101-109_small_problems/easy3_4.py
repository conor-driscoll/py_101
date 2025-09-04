def stringy(positive_int):
    current_digit = '1'
    number_string = ''
    
    for _ in range(positive_int):
        number_string += current_digit
        
        if current_digit == '1':
            current_digit = '0'
        else:
            current_digit = '1'

    return number_string 


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True