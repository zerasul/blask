
class PageNotExistError(Exception):
    def __init__(self, message):
        super(PageNotExistError, self).__init__(message)
