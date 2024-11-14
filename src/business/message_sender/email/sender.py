from utils import BaseService
from src import settings
from typing import Optional
from messages import Email


class EmailSender(BaseService):
    def __init__(
        self,
        username: str = settings.Sender.email,
        password: str = settings.Sender.password,
        *args,
        **kwargs
    ):
        self.username = username
        self.password = password
        super().__init__(*args, **kwargs)

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
