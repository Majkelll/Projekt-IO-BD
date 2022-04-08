from website.scripts.consts.email import EMAIL_ADDRESS
from ... import mail
from flask_mail import Message


def send_email(email: str, title: str, body: str) -> None:
    msg = Message(title,
                  sender=EMAIL_ADDRESS, recipients=[email])
    msg.body = body
    mail.send(msg)
