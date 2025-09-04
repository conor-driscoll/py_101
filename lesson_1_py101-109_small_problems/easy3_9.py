def clean_up(string):
    new_string = ''
    
    for char in string:
        if char.isalpha():
            new_string += char
        elif len(new_string) == 0 or new_string[-1] != ' ':
                new_string += ' '

    return new_string



print(clean_up("---what's my +*& line?") == " what s my line ")
# True