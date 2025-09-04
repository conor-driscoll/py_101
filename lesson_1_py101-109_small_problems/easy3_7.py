def twice(number):
    str_num = str(number)

    if str_num[:int(len(str_num) / 2)] == str_num[int(len(str_num) / 2):]:
        return number
    else:
        return number * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True