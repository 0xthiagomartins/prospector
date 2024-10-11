from pprint import pprint
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
            "abuse@godaddy.com",
            "22@",
            "u0027@",
            "jane.doe@",
            "john.doe@",
        ],
    }

    def _get_from_web_extractors(self, domain: str):
        emails1 = get_emails_from_google(domain)
        emails2 = get_emails_from_bing(domain)
        emails3 = get_emails_from_baidu(domain)
        emails = set(emails1 + emails2 + emails3)
        return list(emails)

    def __filter_emails(self, emails: list[str]) -> list[str]:
        not_in_clauses = set(self.email_filter["not-in"])
        filtered_emails = []

        for email in emails:
            if not any(not_in_clause in email for not_in_clause in not_in_clauses):
                filtered_emails.append(email)
            else:
                for not_in_clause in not_in_clauses:
                    if not_in_clause in email:
                        self._log(not_in_clause)

        return filtered_emails

    def _get_from_whois(self, domain: str):
        data = whois(domain)
        emails = data.get("emails", []) or []
        if type(emails) == str:
            emails = [emails]
        return emails

    def find_from_domain(self, domain: str) -> list[str]:
        extracted_emails = self._get_from_web_extractors(domain)
        whois_emails = self._get_from_whois(domain)
        emails = extracted_emails + whois_emails
        emails = self.__filter_emails(emails)
        return list(set(emails))
