import os, sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typer import Typer, Option
from rich import print
from src.service import Prospector

app = Typer()


@app.command()
def get_emails(domain: str = Option(..., help="The user ID to list conversations for")):
    emails = Prospector(verbose=True).list_emails_from_domain(domain)
    print(", ".join(emails))


if __name__ == "__main__":
    app()
