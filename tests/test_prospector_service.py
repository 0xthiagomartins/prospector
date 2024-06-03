from src.service import Prospector


def test_get_emails_from_domain(domain: str):
    return Prospector(verbose=True).list_emails_from_domain(domain)


if __name__ == "__main__":
    domain = input("Input your domain: ")
    emails = test_get_emails_from_domain(domain)
