from validation import get_validator
from helpers import *
from messages import *
from models import Client, LoginAttempt, BlockedUser, Token
from exceptions import *
from settings import *
import datetime
import smtplib
from local_settings import PASSWORD

class AuthenticationController:
    def __init__(self, session):
        self.session = session
        self.__client_id = None
        self.__username = None
        self.__password = None
        self.__hash_password = None
        self.__salt = None
        self.__email = None

    def __commit(self):
        self.session.commit()

    def _commit_object(self, obj):
        self.session.add(obj)
        self.__commit()

    def _commit_objects(self, objects):
        self.session.add_all(objects)
        self.__commit

    def _get_id(self):
        self.__client_id = self.session.query(Client.id).\
                filter(Client.username == self.__username).one()[0]

    def create_client_info(self):
        user = Client(username=self.__username, password=self.__hash_password,
                      salt=self.__salt, email=self.__email)

        return user

    def create_login_attempt(self, status):
        time = datetime.datetime.now()
        login_attempt = LoginAttempt(attempt_status=status, timestamp=time,
                                     client_id=self.__client_id)
        self._commit_object(login_attempt)

    def check_user_is_in_base(self, username):
        user = self.session.query(Client).\
            filter(Client.username == username).first()

        if user is not None:
            return True

        return False

    def block_user(self):
        block_start = datetime.datetime.now()
        block_end = block_start + datetime.timedelta(seconds=BLOCKING_TIME)
        blocked_user = BlockedUser(block_start=block_start, block_end=block_end,
                                   client_id=self.__client_id)
        self._commit_object(blocked_user)

    def check_password(self, pass2):
        self.__salt = self.session.query(Client.salt).\
            filter(Client.username == self.__username).one()[0]

        self.__hash_password = self.session.query(Client.password).\
            filter(Client.username == self.__username).\
            one()

        hash_pass, s = hash_password(password=pass2, salt=self.__salt)

        return self.__hash_password[0] == hash_pass

    def register(self, username, password, email):
        if self.check_user_is_in_base(username):
            raise ClientAlreadyRegistered('Client already registered')

        validator = get_validator(username)
        if validator.is_valid(password):
            self.__username = username
            self.__password = password
            self.__hash_password, self.__salt = hash_password(password)
            self.__email = email

        user = self.create_client_info()
        self._commit_object(user)

    def login(self, username, password):
        if not self.check_user_is_in_base(username):
            raise ClientNotRegistered('Client is not registered')

        self.__username = username
        self._get_id()

        if self.is_blocked():
            raise UserBlockedException(BLOCKED_MESSAGE)

        if not self.check_password(password):
            self.create_login_attempt(status="FAILED")
            self.block_if_necessary()
            raise WrongPassword("Wrong password")
        else:
            self.create_login_attempt(status="SUCCESS")

    def block_if_necessary(self):
        attempt_statuses = self.session.query(LoginAttempt.attempt_status).\
                           filter(LoginAttempt.client_id == self.__client_id).\
                           order_by(LoginAttempt.timestamp.desc()).\
                           limit(3).all()

        if len(attempt_statuses) < BLOCK_AFTER_N_ATTEMPTS:
            return

        should_block = all([r[0] == 'FAILED' for r in attempt_statuses])

        if not should_block:
            return

        self.create_login_attempt(status='BLOCKED')
        self.block_user()

    def is_blocked(self):
        r = self.session.query(BlockedUser.block_end).\
            filter(BlockedUser.client_id == self.__client_id).\
            order_by(Blocked_users.block_end.desc()).first()

        if r is None:
            return False

        now = datetime.datetime.now()
        return r[0] > now

    def select_email_by_username(self):
        email = self.session.query(Client.email).\
                filter(Client.username == self.__username).\
                one()

        return email[0]

    def add_token_in_tokens(self, unique_token):
        new_token = Token(token=unique_token, client_id=self.__client_id)
        self._commit_object(new_token)

    def send_reset_password(self, username):
        self.__username = username
        self._get_id()
        new_token = generate_salt()
        self.add_token_in_tokens(new_token)

        fromaddr = 'monkovamonika@gmail.com'
        toaddrs = self.select_email_by_username()
        msg = "Your new password is {}".format(new_token)
        username = 'monkovamonika@gmail.com'
        password = PASSWORD
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

    def check_token(self, token2, username):
        self.__username = username
        self._get_id()

        t = self.session.query(Token.token).filter(
            Token.client_id == self.__client_id).order_by(
            Token.id.desc()).one()

        return t == token2

    def update_password(self, username, new_password):
        validator = get_validator(username)
        if validator.is_valid(new_password):
            hash_password, salt = hash_password(password)

        user = self.session.query(Client).filter(
            Client.username == username).one()
        user.password = hash_password
        user.salt = salt
        self._commit_object(user)


class TransactionController:
    def __init__(self, session):
        self.session = session

    def __commit(self):
        return self.session.commit()

    def deposit(self, client, money_amount):
        if money_amount >= 0:
            raise ValueError("You want to deposit invalid sum.")

        user = self.session.query(Client).\
                filter(Client.email == client.email).first()

        if user is None:
            raise NoSuchCLient('There is no such client.')

        user.balance += money_amount
        self.__commit()

    def withdraw(self, client, money_amount):
        if money_amount <= 0:
            raise ValueError("You want to withdraw invalid sum.")

        user = self.session.query(Client).\
                filter(Client.email == client.email).first()

        if user is None:
            raise NoSuchCLient('There is no such client.')

        if user.balance - money_amount < 0:
            raise WithdrawError("You don't have enough money.")
        else:
            user.balance -= money_amount

        self.__commit()

    def display_balance(self, client):
        user = self.session.query(Client).\
                filter(Client.email == client.email).first()
        if user is None:
            raise NoSuchCLient('There is no such client.')

        return "{}$".format(user.balance)