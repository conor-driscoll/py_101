# def oddities(my_list):
#     new_list = []
    
#     for index, element in enumerate(my_list):
#         if index % 2 == 0:
#             new_list.append(element)

#     return new_list


# Bonus question:
# def oddities(my_list):
#     new_list = my_list[0:len(my_list):2]
#     return new_list


# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True



# Further exploration:
def even_stevens(my_list):
    new_list = []
    
    for index, _ in enumerate(my_list):
        if index % 2 == 1:
            new_list += [my_list[index]]

    return new_list


print(even_stevens([2, 3, 4, 5, 6]) == [3, 5])     # True
print(even_stevens([1, 2, 3, 4]) == [2, 4])        # True
print(even_stevens(["abc", "def"]) == ['def'])     # True
print(even_stevens([123]) == [])                   # True
print(even_stevens([]) == [])                      # True