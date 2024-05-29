from pprint import pprint


class BaseService:
    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def _log(self, *args, **kwargs):
        if self.verbose:
            pprint(*args, **kwargs)
