from website.models import User
from website.scripts.auth.signup.check_email import check_email
from website.scripts.auth.signup.check_password import check_password
from website.scripts.consts.signup_messages import *
from datetime import datetime
from .... import db


def validate_data(email, username, password1, password2, birthdate, gender):
    raport = {'status': None, 'content': None}
    current_date = datetime.now()

    if db.session.query(User).filter_by(username=username).first():
        raport['status'] = 'error'
        raport['content'] = WRONG_NAME
        return raport

    if db.session.query(User).filter_by(email=email).first():
        raport['status'] = 'error'
        raport['content'] = WRONG_EMAIL
        return raport

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

    # check if birthdate not in future
    elif not birthdate.date() < current_date.date():
        raport['status'] = 'error'
        raport['content'] = BIRTHDATE_IN_FUTURE
        return raport

    # check gender
    elif gender not in ['m', 'f']:
        raport['status'] = 'error'
        raport['content'] = WRONG_GENDER
        return raport

    else:
        raport['status'] = 'success'
        raport['content'] = ACCOUNT_CREATED
        return raport
