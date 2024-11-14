import os
from dotenv import load_dotenv

print(f'Load .env: {load_dotenv(dotenv_path="./resources/.env")}', flush=True)


class Sender:
    email = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
