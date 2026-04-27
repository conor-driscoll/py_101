numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

def is_list(test_collection):
    print(isinstance(test_collection, list))

is_list(numbers)
is_list(table)