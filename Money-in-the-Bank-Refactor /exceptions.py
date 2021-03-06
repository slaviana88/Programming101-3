class ClientAlreadyRegistered(Exception):
    pass


class ClientNotRegistered(Exception):
    pass


class WrongPassword(Exception):
    pass


class UserBlockedException(Exception):
    pass


class DepositInvalidAmount(Exception):
    pass


class WithdrawError(Exception):
    pass
