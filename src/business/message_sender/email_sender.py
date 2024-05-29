from utils import BaseService
from src import config as cfg
from typing import Optional
from messages import Email


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
    ):
        msg = Email(
            from_=self.username,
            to=to,
            auth=self.password,
            cc=cc,
            bcc=bcc,
            subject=subject,
            body=body,
            attachments=attachments,
            verbose=self.verbose,
        )
        msg.send()
        self._log("Email sent successfully")
        return True
