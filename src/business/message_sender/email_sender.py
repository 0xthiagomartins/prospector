from utils import BaseService
import smtplib, base64
from email.message import EmailMessage
from src import config as cfg
from typing import Optional


class EmailSender(BaseService):
    def __init__(
        self,
        username: str = cfg.Sender.email,
        password: str = cfg.Sender.password,
    ):
        self.username = username
        self.password = password

    def send_email(
        self,
        to: list[str],
        subject: str,
        body: str,
        cc: Optional[list[str]] = None,
        bcc: Optional[list[str]] = None,
        attachments: Optional[list[str, str]] = None,
        html: bool = False,
    ):
        msg = EmailMessage()

        if html:
            msg.add_alternative(body, subtype="html")
        else:
            msg.set_content(body)

        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = ", ".join(to)
        if cc:
            msg["Cc"] = ", ".join(cc)
        if bcc:
            msg["Bcc"] = ", ".join(bcc)

        if attachments:
            for file_name, encoded_content in attachments.items():
                decoded_content = base64.b64decode(encoded_content)
                msg.add_attachment(
                    decoded_content,
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_name,
                )

        with smtplib.SMTP_SSL(cfg.SMTP.server, cfg.SMTP.port) as smtp_conn:
            smtp_conn.login(self.username, self.password)
            smtp_conn.send_message(msg)

        return "Email sent successfully"
