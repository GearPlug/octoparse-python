class InvalidGrantError(Exception):
    pass


class UnsupportedGrantTypeError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class UserNotAllowedError(Exception):
    pass


class NotFoundError(Exception):
    pass


class MethodNotAllowedError(Exception):
    pass


class QuotaExceededError(Exception):
    pass


class ServiceUnavailableError(Exception):
    pass


class UncaughtError(Exception):
    pass
