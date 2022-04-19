# std
import unittest

# test
from rustlike import resultify, Ok, Err


class TestResultify(unittest.TestCase):

    def test_ok(self):
        @resultify()
        def func():
            return 1
        res = func()
        self.assertIsInstance(res, Ok)

    def test_err_handled(self):
        @resultify()
        def func():
            raise ValueError('value error')
        res = func()
        self.assertIsInstance(res, Err)
