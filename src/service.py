from utils import BaseService
from src.business.contact_finder import EmailFinder


class Prospector(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def list_opportunities(self):
        pass

    def list_emails_from_domain(self, domain):
        return EmailFinder(verbose=self.verbose).find_from_domain(domain)
