import typer
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_emails(domain: str):
    from src.service import Prospector

    def emails_to_string(email_list):
        return ", ".join(email_list)

    emails = Prospector(verbose=True).list_emails_from_domain(domain)
    print(emails_to_string(emails))


if __name__ == "__main__":
    typer.run(get_emails)
