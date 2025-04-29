# A function that returns the sum of two numbers:
# Casual pseudocode -
# Define a function with an informative name, which takes two inputs
# Instruct the program to add the two numbers, and output the result
# Formal pseudocode -
# Define an informatively-named function which takes two arguments
# Return the result of the arguments placed on either side of an addition sign
# 
# A function that takes a list of strings, and returns a string that is all 
# those strings concatenated together: 
# Casual pseudocode -
# Define a function with an informative name, which takes one input
# Instruct the function to attach the first string to the second string,
# attach the third to the resulting string, and so on, until all the strings
# in the list have been joined together (ensure that empty and one-item lists
# can be accommodated)
# Return the result
# Formal pseudocode -
# Define a function with an informative name, which takes one argument
# set a concat_list variable equal to an empty string 
# Use a for loop and the len function to iterate through the entire list,
# concatenating all the strings in the list to the concat_list variable, one
# item at a time (ensuring that empty and one-item lists can be accommodated)
# Return the final value of the concat_list variable
# 
# A function that takes a list of integers, and returns a new list with every
# other element from the original list, starting with the first element:
# Casual pseudocode -
# Define a function with an informative name, which takes one list input 
# Instruct the function to take every other item from a list of integers, and 
# return a new list with only these select items
# Formal pseudocode -
# Define a function with an informative name, which takes one list argument
# Use a for loop with a range of (0, len(list), 2), to iterate through the
# original list, and add the selected items, one at a time, to an initially-
# empty list
# Return this resulting list 
# 
# A function that determines the index of the 3rd occurrence of a given
# character in a string. For instance, if the given character is 'x' and the 
# string is 'axbxcdxex', the function should return 6 (the index of the 3rd 
# 'x'). If the given character does not occur at least 3 times, return None:
# Casual pseudocode -
# Define a function with an informative name, which takes one string input
# Instruct the function to determine the third occurrence of a given character
# in a string, and return the index value for this occurrence
# Formal pseudocode -         
# Define a function with an informative name, which takes one string argument
# Set an iterator variable equal to 0 
# Use the str.find method to search for the first occurrence of the given
# character
# If the character is found, 1 will be added to the iterator, and the next
# str.find search will take place starting at the index value of the first
# occurrence, plus 1. 
# If the character is found again, this process will be repeated until the 
# iterator value reaches three, at which point the latest value of the str.find
# function will be returned 
# If the character isn't found at any point in this process, the str.find 
# method will return -1, and our function will take that as a cue to return
# None
# 
# A function that takes two lists of numbers and returns the result of merging 
# the lists. The elements of the first list should become the elements at the 
# even indexes of the returned list, while the elements of the second list 
# should become the elements at the odd indexes. 
# Casual pseudocode -
# Define a function with an informative name, which takes two list inputs
# Instruct the function to merge the two lists into a single list, such that
# the items in the first list become the items at the even indexes of the
# resulting list, and the items in the second list become the items at the 
# odd indexes of the resulting list
# Return the resulting list
# Formal pseudocode -         
# Define a function with an informative name, which takes two list arguments
# Set a merged_list variable with an empty list as its value
# Iterate using a for loop with range(len(either list))
# Inside this for loop, the range value will become the index value used to
# first select an item from the first list, and then one from the second list,
# for these items to be sequentially added to the merged_list
# Return merged_list