import unittest
import time
from decorators import accepts, encrypt, log, performance
from subprocess import check_output


def call_solution(filename):
    command = "cat {}".format(filename)

    return check_output(["/bin/bash", "-c", command])\
        .decode('utf-8').strip()


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    return "{} save {}".format(name, money)


@log("log.txt")
@encrypt(2)
def get_low():
    return "Get get get low"


@performance('file.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


class TestAccepts(unittest.TestCase):

    def test_accepts_with_one_arg(self):
        expected = "Hello, I am Rado"
        self.assertEqual(say_hello("Rado"), expected)

    def test_accepts_throws_exception(self):
        expected = "Argument 1 of say_hello is not str!"
        self.assertRaisesRegexp(TypeError, expected, say_hello, 2)

    def test_accepts_with_2_agrs(self):
        expected = "Rado save 20"
        self.assertEqual(deposit("Rado", 20), expected)

    def test_deposit_exc(self):
        expected = "Argument 2 of deposit is not int!"
        self.assertRaisesRegexp(TypeError, expected, deposit, "Rado", "Ivo")


class TestEncryptLog(unittest.TestCase):

    def test_encrypt(self):
        expected = "Igv igv igv nqy"
        self.assertEqual(get_low(), expected)

    def test_log(self):
        expected = "get_low was called at"
        get_low()

        output = call_solution("log.txt")
        self.assertTrue(expected in output)


class TestPerformance(unittest.TestCase):

    def test_performance(self):
        expected = "something_heavy was called"
        something_heavy()

        output = call_solution("file.txt")
        self.assertTrue(expected in output)

if __name__ == '__main__':
    unittest.main()
