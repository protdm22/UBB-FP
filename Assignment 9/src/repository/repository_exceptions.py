class RepositoryException(Exception):
    def __init__(self, error_details):
        self._error_message = "REPOSITORY ERROR! " + error_details

    def __str__(self):
        return self._error_message

class ObjectAlreadyExistsException(RepositoryException):
    def __init__(self, error_details):
        super().__init__(error_details)

class ObjectNotFoundException(RepositoryException):
    def __init__(self, error_details):
        super().__init__(error_details)

