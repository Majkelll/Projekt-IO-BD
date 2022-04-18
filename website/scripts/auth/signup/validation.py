from website.scripts.auth.signup.check_email import check_email
from website.scripts.auth.signup.check_password import check_password
from website.scripts.consts.signup_messages import *
from datetime import datetime


def validate_data(email, username, password1, password2, birthdate):
    raport = {'status': None, 'content': None}
    current_date = datetime.now()

    # check if email correct
    if not check_email(email):
        raport['status'] = 'error'
        raport['content'] = WRONG_EMAIL
        return raport

    # check username
    elif len(username) < 2:
        raport['status'] = 'error'
        raport['content'] = WRONG_NAME
        return raport

    # check if password the same
    elif password1 != password2:
        raport['status'] = 'error'
        raport['content'] = DIFFERENT_PASSWORDS
        return raport

    # check password
    elif not check_password(password1):
        raport['status'] = 'error'
        raport['content'] = PASSWORD_TOO_WEAK
        return raport

    # check birthdate
    elif not birthdate.date() < current_date.date():
        raport['status'] = 'error'
        raport['content'] = BIRTHDATE_IN_FUTURE
        return raport

    else:
        raport['status'] = 'success'
        raport['content'] = ACCOUNT_CREATED
        return raport
