import sql_manager
import sys
import getpass


class Commands:

    @classmethod
    def start(cls):
        print("""Welcome to our bank service. You are not logged in.
    All available commands:
    register, login, list, help, exit

    Please, register or login""")

    @classmethod
    def register(cls):
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ", stream=None)

        sql_manager.register(username, password)
        print("Registration is successfull!")

    @classmethod
    def login(cls):
        username = input("Enter your username: ")
        password = getpass.getpass(stream=None)

        logged_user = sql_manager.login(username, password)

        if logged_user:
            cls.logged_menu(logged_user)
        else:
            print("Login failed")

        return username

    @classmethod
    def help(cls):
        print("login - for logging in!")
        print("register - for creating new account!")
        print("exit - for closing program!")

    @classmethod
    def exit(cls):
        sys.exit("You are out of your account.")

    @classmethod
    def list(cls):
        print("""        All available commands:
        register, login, list, help, exit""")


    @classmethod
    def logged_menu(logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        print("""Available commands: info/change-pass/change-message/
            show-message/help""")

        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'change-pass':
                new_pass = input("Enter your new password: ")
                sql_manager.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                sql_manager.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")
