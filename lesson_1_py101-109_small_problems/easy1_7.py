def short_long_short(string1, string2):
    if len(string1) > len(string2):
        long_string, short_string = string1, string2
    else:
        long_string, short_string = string2, string1
    
    return short_string + long_string + short_string

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")