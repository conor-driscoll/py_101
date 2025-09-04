def center_of(string):
    half_len_int = int(len(string) / 2)
    
    if len(string) % 2 == 1:
        return string[half_len_int] # int function rounds down
    else:
        return string[half_len_int - 1:half_len_int + 1]    

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True