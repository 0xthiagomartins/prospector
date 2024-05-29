from utils import BaseService
from emailfinder.extractor import (
    get_emails_from_google,
    get_emails_from_bing,
    get_emails_from_baidu,
)
from whois import whois


class EmailFinder(BaseService):
    email_filter = {
        "not-in": [
            "@publicdomainregistry.com",
            "@privacyprotect.org",
        ],
    }

    def _get_from_web_extractors(self, domain: str):
        emails1 = get_emails_from_google(domain)
        emails2 = get_emails_from_bing(domain)
        emails3 = get_emails_from_baidu(domain)
        emails = set(emails1 + emails2 + emails3)
        return list(emails)

    def __filter_emails(self, emails: list[str]):
        filtered_emails = []
        for email in emails:
            for not_in_clause in self.email_filter["not-in"]:
                if not_in_clause not in email:
                    filtered_emails.append(email)

        return filtered_emails

    def _get_from_whois(self, domain: str):
        data = whois(domain)
        emails = data.get("emails", []) or []
        emails = self.__filter_emails(emails)
        return emails

    def find_from_domain(self, domain: str) -> list[str]:
        extracted_emails = self._get_from_web_extractors(domain)
        whois_emails = self._get_from_whois()
        emails = set(extracted_emails + whois_emails)
        return list(emails)
