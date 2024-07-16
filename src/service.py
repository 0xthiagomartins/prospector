from utils import BaseService
from src.business.contact_finder import EmailFinder
from src.business.message_sender import EmailSender, Template
from .config import *


class Prospector(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def list_opportunities(self):
        pass

    def list_emails_from_domain(self, domain):
        return EmailFinder(verbose=self.verbose).find_from_domain(domain)

    def send_email(self, emails, template: str = "job_opportunity"):
        template = Template(name=template)
        return EmailSender().send_email(emails, template)
