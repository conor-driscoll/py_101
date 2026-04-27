str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

substr1 = "Dino"

def substring_in_string(substring, string):
    print(substring in string)

substring_in_string(substr1, str1)
substring_in_string(substr1, str2)