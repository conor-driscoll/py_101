CHARACTER_LIMIT = 40

title1 = "Flintstone Family Members"
title2 = "Flintstone Family Member"


def align_title_with_spaces(title_argument):
    if (CHARACTER_LIMIT - len(title_argument)) % 2 == 0:
        print ((int((CHARACTER_LIMIT - len(title_argument)) / 2) * ' ') + title_argument)
    else:
        print ((((CHARACTER_LIMIT - len(title_argument)) // 2) * ' ') + title_argument)


align_title_with_spaces(title1)
align_title_with_spaces(title2)

print(title1.center(40))
print(title2.center(40))