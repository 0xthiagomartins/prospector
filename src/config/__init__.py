import os


class Sender:
    email = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("SENDER_PASSWORD")
