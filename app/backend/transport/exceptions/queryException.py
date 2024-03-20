

class QueryException(Exception):

    def __init__(self, code, **kwargs):

        messageBuilder = dict(map(lambda x: (x, "is missing"), filter(lambda x: not kwargs[x] ,kwargs)))

        self.message = messageBuilder
        self.code = code
        super().__init__(self.message)