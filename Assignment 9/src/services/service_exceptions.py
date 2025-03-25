class ServiceException(Exception):
    def __init__(self, error_details):
        self._error_message = "SERVICE ERROR! " + error_details

    def __str__(self):
        return self._error_message


class NoMatchingSearches(ServiceException):
    def __init__(self, error_details):
        super().__init__(error_details)

class IDNotFoundException(ServiceException):
    def __init__(self, error_details):
        super().__init__(error_details)