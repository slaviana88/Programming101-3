import unittest
from BankAcc import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Rosko", 10, "BGN")

    def test_create_bank_account_class(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_is_name_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount(1000, 10, "BGN")

    def test_is_balance_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount("Rosko", "gosho", "BGN")

    def test_is_currency_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount("Rosko", 100, 1000)

    def test_is_balance_positive_number(self):
        with self.assertRaises(ValueError):
            BankAccount("Rosko", -10, "BGN")

    def test_is_balance_private(self):
        with self.assertRaises(AttributeError):
            self.account.balance += 10

    def test_is_amount_being_deposited(self):
        old_balance = self.account.get_balance()
        self.account.deposit(10)
        new_balance = self.account.get_balance()
        self.assertEqual(10, new_balance - old_balance)

    def test_is_withdraw_possible_with_negative_number(self):
        self.assertFalse(self.account.withdraw(-10))

    def test_is_withdraw_possible_if_balance_not_enough(self):
        self.assertFalse(self.account.withdraw(20))

    def test_is_amount_multiple_by_10(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(5)

    def test_account_str_print(self):
        self.assertEqual(str(self.account), "Bank account for Rosko with balance of 10BGN")

    def test_account_int_return(self):
        self.assertEqual(int(self.account), 10)

    def test_is_trasfer_possible_if_accounts_have_different_currencies(self):
        kiro = BankAccount("Kiro", 50, "$")
        self.assertFalse(self.account.transfer_to(kiro, 100))

if __name__ == '__main__':
    unittest.main()
