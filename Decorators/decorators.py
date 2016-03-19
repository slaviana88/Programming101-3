import datetime
from functools import wraps
# from time import strftime
# import time
# from random import randint


def accepts(*arguments):
    def accepter(func):
        def decorated(*argv):
            if len(argv) != len(arguments):
                raise TypeError("No enough arguments")
            for index, (argument, f_argv) in enumerate(zip(arguments, argv)):
                if not isinstance(f_argv, argument):
                    raise TypeError("Argument {} of {} is not {}!".format(
                                                    index+1,
                                                    func.__name__,
                                                    argument.__name__))
            return func(*argv)
        return decorated
    return accepter


def encode(string, number):
    result = ""
    for symbol in string:
        if symbol is not " ":
            result += chr(ord(symbol) + number)
        else:
            result += " "
    return result


def encrypt(number):
    def accepter(func):
        @wraps(func)
        def decorator():
            string = func()
            result = encode(string, number)
            return result
        return decorator
    return accepter


def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorator():
            with open(file_name, "a") as myfile:
                myfile.write('{} was called at {}\n'.format(
                                                func.__name__,
                                                datetime.datetime.now().time()))
                myfile.close()
            return func()
        return decorator
    return accepter


# def performance(file_name):
#     def accepter(func):
#         def decorator():
#             startTime = strftime("%H:%M:%S")
#             s = startTime.split(':')
#             func()
#             endTime = strftime("%H:%M:%S")
#             e = endTime.split(':')
#             array = zip(e, s)
#             time = 0
#             for el in array:
#                 time += int(el[0]) - int(el[1])
#             with open(file_name, "a") as myfile:
#                 myfile.write('''{} was called and took
#                              {} seconds to complete\n'''.format(
#                                                 func.__name__,
#                                                 time))
#         return decorator
#     return accepter
