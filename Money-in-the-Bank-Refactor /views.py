from controller import ClientAlreadyRegistered, WrongPassword, ClientNotRegistered, UserBlockedException
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
                    print("Lqlq")
                    token = input('Check your email and write token: ')
                    if self.controller.check_token(username, token):
                        new_password = input('New password: ')
                        self.controller.update_password(username, new_password)
                except Exception as e:
                    print(e)