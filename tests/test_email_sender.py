import base64
from src.business.message_sender import EmailSender


def test_send_email():
    sender = EmailSender(verbose=True)
    sender.send_email(
        to=["foo.bar@bar.com"],
        subject="Test Email",
        body="<h1>Hello, World!</h1>",
        cc=["foo@bar.com"],
        # bcc=["bcc@example.com"],
        attachments={
            "utils.py": "./src/business/utils.py",
        },
    )
