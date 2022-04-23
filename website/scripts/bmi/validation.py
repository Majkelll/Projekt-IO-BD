from website.scripts.consts.bmi_form_errors import *
from datetime import datetime, date


def validate_bmi_form(weight, height, birthdate, gender):
    raport = {'status': None, 'content': None}

    # check if weight is float number
    try:
        weight = float(weight)
    except:
        raport['status'] = 'error'
        raport['content'] = WRONG_WEIGHT
        return raport

    # check if weight is float number
    try:
        height = float(height)
    except:
        raport['status'] = 'error'
        raport['content'] = WRONG_HEIGHT
        return raport

    # check if birthdate not in future
    current_date = datetime.now()
    if not birthdate < current_date.date():
        raport['status'] = 'error'
        raport['content'] = BIRTHDATE_IN_FUTURE
        return raport

    # check gender
    elif not gender in ['m', 'f']:
        raport['status'] = 'error'
        raport['content'] = WRONG_GENDER
        return raport

    else:
        raport['status'] = 'success'
        raport['content'] = ""
        return raport
