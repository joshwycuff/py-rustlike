# std
import unittest

# test
from rustlike import option
from rustlike.rustlike import Option, Some, NONE_OPT, OptionException
from rustlike.rustlike import Result, Ok, Err


class TestResult(unittest.TestCase):
    some = Some(1)
    none = NONE_OPT

    def test_new_some(self):
        x = option(1)
        self.assertIsInstance(x, Option)
        self.assertIsInstance(x, Some)

    def test_new_none(self):
        x = option()
        self.assertIsInstance(x, Option)
        self.assertNotIsInstance(x, Some)

    # Querying the variant

    def test_some_is_some(self):
        some = option(1)
        self.assertTrue(some.is_some())

    def test_some_not_is_none(self):
        some = option(1)
        self.assertFalse(some.is_none())

    def test_none_not_is_some(self):
        none = option()
        self.assertFalse(none.is_some())

    def test_none_is_none(self):
        some = option()
        self.assertTrue(some.is_none())

    # Extracting the contained value

    def test_expect_some(self):
        some = option(1)
        self.assertEqual(1, some.expect(''))

    def test_expect_none(self):
        none = option()
        with self.assertRaises(OptionException):
            none.expect('')

    def test_expect_custom_error(self):
        none = option()
        with self.assertRaises(ValueError):
            none.expect(ValueError(''))

    def test_unwrap_some(self):
        some = option(1)
        self.assertEqual(1, some.unwrap())

    def test_unwrap_none(self):
        none = option()
        with self.assertRaises(OptionException):
            none.unwrap()

    def test_unwrap_or_some(self):
        some = option(1)
        self.assertEqual(1, some.unwrap_or(2))

    def test_unwrap_or_none(self):
        none = option()
        self.assertEqual(2, none.unwrap_or(2))

    # Transforming contained values

    def test_some_ok_or(self):
        some = option(1)
        res = some.ok_or(ValueError(''))
        self.assertIsInstance(res, Ok)
        self.assertEqual(1, res.unwrap())

    def test_none_ok_or(self):
        none = option()
        res = none.ok_or(ValueError(''))
        self.assertIsInstance(res, Err)

    # bool

    def test_some_truthy(self):
        self.assertTrue(self.some)

    def test_none_falsy(self):
        self.assertFalse(self.none)
