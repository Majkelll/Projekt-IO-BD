def calculate_bmi(weight, height):
    height /= 100
    return round(weight / (height ** 2), 1)


def calculate_bmr(gender, weight, height, age):
    if gender == 'm':
        return 66 + (13.7 * weight) + (5 * height) - (6.67 * age)
    elif gender == 'f':
        return 655 + (9.7 * weight) + (1.8 * height) - (4.77 * age)
