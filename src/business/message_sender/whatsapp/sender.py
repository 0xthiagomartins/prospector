from utils import BaseService


class WhatsappSender(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_message(self):
        return
