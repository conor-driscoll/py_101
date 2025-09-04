# def penultimate(string):
#     word_list = string.split()
#     return word_list[-2]

# # These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")


# Further exploration:
# Edge cases -
# - if even number of words, return two middle words in a tuple
# - if one word, return that word
# - if empty string, return empty string

def middle(string):
    word_list = string.split()
    
    if not string:    # if empty string
        return string

    if len(word_list) == 1:
        return word_list[0]

    if len(word_list) % 2 == 0:
        return (word_list[int(len(word_list) / 2) - 1],
                word_list[int(len(word_list) / 2)])

    else:
        return(word_list[len(word_list) // 2])

print(middle('') == '')
print(middle('bonkers') == 'bonkers')
print(middle('bonkers babboons babbling borishly') == ('babboons', 'babbling'))
print(middle('badly bonkers babboons babbling borishly') == 'babboons')