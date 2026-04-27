famous_quote_ending = "seven years ago..."
missing_beginning = "Four score and "


def quote_finisher_concatenation(missing_beginning_argument,
                                 famous_quote_ending_argument):
    print(missing_beginning_argument + famous_quote_ending_argument)

def quote_finisher_interpolation(missing_beginning_argument,
                                 famous_quote_ending_argument):
    print(f'{missing_beginning_argument}{famous_quote_ending_argument}')

def quote_finisher_join(missing_beginning_argument,
                        famous_quote_ending_argument):
    
    complete_quote_list = [missing_beginning_argument,
                           famous_quote_ending_argument]

    print(''.join(complete_quote_list)) 


quote_finisher_concatenation(missing_beginning, famous_quote_ending)
quote_finisher_interpolation(missing_beginning, famous_quote_ending)
quote_finisher_join(missing_beginning, famous_quote_ending)