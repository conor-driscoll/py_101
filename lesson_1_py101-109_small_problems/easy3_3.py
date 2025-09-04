# def print_in_box(string):
#     len_str_2 = len(string) + 2
    
#     print('+' + ('-' * len_str_2) + '+')

#     print('|' + (' ' * len_str_2) + '|')

#     print('| ' + string + ' |')

#     print('|' + (' ' * len_str_2) + '|')

#     print('+' + ('-' * len_str_2) + '+')


# Further exploration 1:
# def print_in_box(string, max_char=42):
    
#     if len(string) > max_char:
#         string = string[0:max_char]
    
#     len_str_2 = len(string) + 2
    
#     print('+' + ('-' * len_str_2) + '+')

#     print('|' + (' ' * len_str_2) + '|')

#     print('| ' + string + ' |')

#     print('|' + (' ' * len_str_2) + '|')

#     print('+' + ('-' * len_str_2) + '+')


# Further exploration 2:
# def print_in_box(string, max_char=42):

#     if len(string) < max_char:
#         len_str_2 = len(string) + 2
#     else:
#         len_str_2 = max_char + 2

#     print('+' + ('-' * len_str_2) + '+')
#     print('|' + (' ' * len_str_2) + '|')

#     if len(string) % max_char != 0:
#         str_num = (len(string) // max_char) + 1
#     else:
#         str_num = len(string) // max_char

#     if str_num == 0:
#         print('|' + (' ' * len_str_2) + '|')

#     current_index_start = 0
#     for current_num in range(str_num):
#         if current_num == str_num - 1:
#             current_string = string[current_index_start:]
#             if str_num > 1:
#                 current_string += (' ' * (max_char - len(current_string)))
#         else:
#             current_string = string[current_index_start:
#                                     (current_index_start + max_char)]
#             current_index_start += max_char
            
#         print('| ' + current_string + ' |')
        
#     print('|' + (' ' * len_str_2) + '|')
#     print('+' + ('-' * len_str_2) + '+')
   

# print_in_box('To boldly go where no one has gone before, and no one will go'
#              'again in this millenium.', 20)
# print_in_box('To boldly go where no one has gone before.', 20)
# print_in_box('To boldly go.', 20)
# print_in_box('', 20)


def print_in_box():

    print("\nWelcome to Owlman's banner printing program!\n")
    
    string = input("Please enter the text that you'd like to bannerize!\n")

    max_char = int(input("\nPlease enter a positive integer for your maximum"
                         "character limit per line: "))

    if len(string) < max_char:
        len_str_2 = len(string) + 2
    else:
        len_str_2 = max_char + 2

    print('\n+' + ('-' * len_str_2) + '+')
    print('|' + (' ' * len_str_2) + '|')

    if len(string) % max_char != 0:
        str_num = (len(string) // max_char) + 1
    else:
        str_num = len(string) // max_char

    if str_num == 0:
        print('|' + (' ' * len_str_2) + '|')

    current_index_start = 0
    for current_num in range(str_num):
        if current_num == str_num - 1:
            current_string = string[current_index_start:]
            if str_num > 1:
                current_string += (' ' * (max_char - len(current_string)))
        else:
            current_string = string[current_index_start:
                                    (current_index_start + max_char)]
            current_index_start += max_char
            
        print('| ' + current_string + ' |')
        
    print('|' + (' ' * len_str_2) + '|')
    print('+' + ('-' * len_str_2) + '+')


print_in_box()