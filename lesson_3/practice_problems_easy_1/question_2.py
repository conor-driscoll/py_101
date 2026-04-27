str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def exclamation_mark_final_character(test_string):
    print(test_string.endswith('!'))

# def exclamation_mark_final_character(test_string):
#     if test_string[-1] == '!':
#         print(True)
#     else:
#         print(False)

# def exclamation_mark_final_character(test_string):
#     if test_string.endswith('!'):
#         print(True)
#     else:
#         print(False)


exclamation_mark_final_character(str1)
exclamation_mark_final_character(str2)