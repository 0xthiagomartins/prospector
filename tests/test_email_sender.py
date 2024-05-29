import base64
from src.business.message_sender import EmailSender


def test_send_email():
    with open("./src/business/utils.py", "rb") as file:
        encoded_content = base64.b64encode(file.read())
    base64_content_utils = encoded_content.decode("utf-8")

    sender = EmailSender()
    sender.send_email(
        to=["foo.bar@bar.com"],
        subject="Test Email",
        body="<h1>Hello, World!</h1>",
        cc=["foo@bar.com"],
        # bcc=["bcc@example.com"],
        attachments={
            "utils2.py": base64_content_utils,
            "utils.py": base64_content_utils,
        },
        html=True,
    )
