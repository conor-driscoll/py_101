def century(year):
    if year % 100 != 0: 
        century_num = (year // 100) + 1
    else:
        century_num = year // 100

    str_cen_num = str(century_num)
    last_char = str_cen_num[-1]
    if len(str_cen_num) > 1:
        sec_last_char = str_cen_num[-2]
    else:
        sec_last_char = '0'
    
    if last_char in ('1', '2', '3') and sec_last_char != '1':
        match last_char:
            case '1':
                return str_cen_num + 'st'
            case '2':
                return str_cen_num + 'nd'
            case '3':
                return str_cen_num + 'rd'
    else:
        return str_cen_num + 'th'

    
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

# print(century(2000))          
# print(century(2001))          
# print(century(1965))          
# print(century(256))           
# print(century(5))             
# print(century(10103))        
# print(century(1052))          
# print(century(1127))          
# print(century(11201))        