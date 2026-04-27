def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# No, these functions won't return the same values, since the first() function
# returns a dictionary, but the second() function returns None, since there's
# nothing after the return keyword, on its same line.