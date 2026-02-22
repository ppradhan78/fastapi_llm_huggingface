class AppException(Exception):
    """Base application exception."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class ConfigurationException(AppException):
    pass


class ExternalServiceException(AppException):
    pass


class ValidationException(AppException):
    pass