from emailfinder.extractor import *


domain = input("Input a domain: ")  # Eg. nassim.com.br
emails1 = get_emails_from_google(domain)
emails2 = get_emails_from_bing(domain)
emails3 = get_emails_from_baidu(domain)
emails = set(emails1 + emails2 + emails3)


def emails_to_string(email_list):
    return ", ".join(email_list)


print(emails_to_string(emails))
