import unittest

from validate_pw_complexity import *

class Test_PW_Functions(unittest.TestCase):

    def test_pw_not_long_enough_min(self):
        sample_pass ="abcd"
        expected_result = False

        result = validate_pw_long(sample_pass)
        self.assertEqual(expected_result, result)

    def test_pw_just_long_enough_min(self):
        sample_pass = "abcdadca"
        expected_result = False

        result = validate_pw_long(sample_pass)
        self.assertEqual(expected_result, result)

    def test_pw_long_enough_min(self):
        sample_pass = "abcdadcaabc"
        expected_result = False

        result = validate_pw_long(sample_pass)
        self.assertEqual(expected_result, result)
