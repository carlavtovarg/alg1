import unittest

class Test(unittest.TestCase):

    def test_regex_condition_1(self):
        input_value = "jim"
        regex = "^jim$"

        self.assertRegex(input_value, regex)

    def test_regex_condition_2(self):
        input_value = "jtm"
        regex = "^jim$"

        self.assertRegex(input_value, regex)

