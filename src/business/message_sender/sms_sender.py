from utils import BaseService


class SMSSender(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_message(self):
        return
