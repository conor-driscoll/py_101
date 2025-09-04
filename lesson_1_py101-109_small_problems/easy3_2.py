# def crunch(string):
#     if string == '':
#         return string
    
#     new_string = string[0]
#     for index, char in enumerate(string):
#         if char != new_string[-1]:
#             new_string += char
    
#     return new_string


# Further exploration:
def crunch(string):
    if string == '':
        return string
    
    for index, char in enumerate(string):
        if index == 0:
            new_string = string[index]
        if char != new_string[-1]:
                new_string += char
    
    return new_string


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')