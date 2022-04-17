from flask_mail import Message

from website.scripts.consts.email import EMAIL_ADDRESS
from ... import mail


def send_email(to: str, subject: str, body: str) -> None:
    msg = Message(subject, sender=EMAIL_ADDRESS,
                  recipients=[to])
    msg.body = body
    try:
        mail.send(msg)
    except Exception as e:
        print("[ERROR][EMAIL]", e)
