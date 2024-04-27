import unittest
from palindrome import palindrome


class palindrome_test(unittest.TestCase):

    def test_palindrome(self):

        self.assertEqual(palindrome('civic'), True)
        self.assertEqual(palindrome('team'), False)
