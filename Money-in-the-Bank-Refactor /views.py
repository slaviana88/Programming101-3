from controller import ClientAlreadyRegistered, WrongPassword, ClientNotRegistered, \
                        UserBlockedException, DepositInvalidAmount, WithdrawError
from validation import StrongPasswordException
import getpass


class MainView:
    def __init__(self, auth_controller, transaction_controller):
        self.controller = auth_controller
        self.transaction_controller = transaction_controller

    def render(self):
        while True:
            command = input('Enter command>')

            if command == 'register':
                username = input('Username:')
                password = getpass.getpass("Enter your password: ")
                email = input('Email: ')

                try:
                    self.controller.register(username, password, email)
                    print('Success registration!')
                except ClientAlreadyRegistered as e:
                    print(e)
                except StrongPasswordException as e:
                    print(e)

            if command == 'login':
                username = input('Username:')
                password = getpass.getpass("Enter your password: ")

                try:
                    self.controller.login(username, password)
                    print('You are login as {}'.format(username))
                    self.main_menu(username)
                except WrongPassword as e:
                    print(e)
                except ClientNotRegistered as e:
                    print(e)
                except UserBlockedException as e:
                    print(e)

            if command == 'exit':
                break

            if command == 'send-reset-password':
                username = input('Username: ')

                try:
                    self.controller.send_reset_password(username)
                    token = input('Check your email and write token: ')
                    if self.controller.check_token(username, token):
                        new_password = input('New password: ')
                        self.controller.update_password(username, new_password)
                except Exception as e:
                    print(e)

    def main_menu(self, username):
        while True:
            command = input("Logged>>> ")

            if command == 'deposit':
                money = input("Enter amount: ")

                try:
                    self.transaction_controller.deposit(username, money)
                except DepositInvalidAmount as e:
                    print(e)

            if command == 'withdraw':
                money = input("Enter amount: ")

                try:
                    self.transaction_controller.withdraw(username, money)
                except WithdrawError as e:
                    print(e)

            if command == 'balance':
                try:
                    print(self.transaction_controller.balance(username))
                except:
                    pass

            if command == 'exit':
                break