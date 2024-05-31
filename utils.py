from pprint import pprint


def emails_to_string(email_list):
    return ", ".join(email_list)


class BaseService:
    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def _log(self, *args, **kwargs):
        if self.verbose:
            pprint(*args, **kwargs)
