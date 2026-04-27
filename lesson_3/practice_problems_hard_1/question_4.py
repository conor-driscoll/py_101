str1 = ''
str2 = '-1.1.1.1'
str3 = '0.0.255.1'
str4 = '1.a.a.1'
str5 = '1.1.1'
str6 = '1.1.1.1.1'
str7 = '1.1.256.1'


def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
        
    return True


print(is_dot_separated_ip_address(str1))
print(is_dot_separated_ip_address(str2))
print(is_dot_separated_ip_address(str3))
print(is_dot_separated_ip_address(str4))
print(is_dot_separated_ip_address(str5))
print(is_dot_separated_ip_address(str6))
print(is_dot_separated_ip_address(str7))