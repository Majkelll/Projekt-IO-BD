from website.scripts.consts.bmi_stages import *


def bmi_summary(bmi):
    if bmi < 18.5:
        return UNDERWEIGHT
    elif bmi >= 18.5 and bmi < 25:
        return NORMAL
    elif bmi >= 25 and bmi < 30:
        return OVERWEIGHT
    elif bmi >= 30 and bmi < 35:
        return OBESE
    elif bmi >= 35:
        return EXTREMELY_OBESE
