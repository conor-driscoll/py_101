def get_grade(score_1, score_2, score_3):
    grade_lst = [score_1, score_2, score_3]
    score_mean = sum(grade_lst) / 3

    if 90 <= score_mean <= 100:
        return 'A'
    elif 80 <= score_mean < 90:
        return 'B'
    elif 70 <= score_mean < 80:
        return 'C'
    elif 60 <= score_mean < 70:
        return 'D'
    else:
        return 'F'


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True