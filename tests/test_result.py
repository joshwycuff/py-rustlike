# std
import unittest

# test
from rustlike.rustlike import result, resultify, Result, Ok, Err, ResultException
from rustlike.rustlike import Option, Some, NoneOpt


class TestResult(unittest.TestCase):
    ok = Ok(1)
    err = Err(ValueError(''))

    # creating new results

    def test_ok_result(self):
        res = result(1)
        self.assertIsInstance(res, Result)
        self.assertIsInstance(res, Ok)

    def test_err_result(self):
        res = result(ValueError(''))
        self.assertIsInstance(res, Result)
        self.assertIsInstance(res, Err)

    def test_result_not_nested(self):
        res = result(result(1))
        self.assertIsInstance(res, Result)
        self.assertIsInstance(res, Ok)
        self.assertEqual(1, res.unwrap())

    # Querying the variant

    def test_ok_is_ok(self):
        res = result(1)
        self.assertTrue(res.is_ok())

    def test_ok_is_err(self):
        res = result(1)
        self.assertFalse(res.is_err())

    def test_err_is_ok(self):
        res = result(ValueError(''))
        self.assertFalse(res.is_ok())

    def test_err_is_err(self):
        res = result(ValueError(''))
        self.assertTrue(res.is_err())

    # Extracting contained values

    def test_ok_expect(self):
        self.assertEqual(1, self.ok.expect(''))

    def test_err_expect(self):
        with self.assertRaises(ResultException):
            self.err.expect('')

    def test_err_expect_custom(self):
        with self.assertRaises(TypeError):
            self.err.expect(TypeError(''))

    def test_ok_unwrap(self):
        self.assertEqual(1, self.ok.unwrap())

    def test_err_unwrap(self):
        with self.assertRaises(ResultException):
            self.err.unwrap()

    def test_ok_unwrap_or(self):
        self.assertEqual(1, self.ok.unwrap_or(2))

    def test_err_unwrap_or(self):
        self.assertEqual(2, self.err.unwrap_or(2))

    # Transforming contained values

    def test_ok_ok(self):
        opt = self.ok.ok()
        self.assertIsInstance(opt, Option)
        self.assertIsInstance(opt, Some)
        self.assertEqual(1, opt.unwrap())

    def test_ok_err(self):
        opt = self.ok.err()
        self.assertIsInstance(opt, Option)
        self.assertIsInstance(opt, NoneOpt)

    def test_err_ok(self):
        opt = self.err.ok()
        self.assertIsInstance(opt, Option)
        self.assertIsInstance(opt, NoneOpt)

    def test_err_err(self):
        opt = self.err.err()
        self.assertIsInstance(opt, Option)
        self.assertIsInstance(opt, Some)
        self.assertIsInstance(opt.unwrap(), ValueError)

    # bool

    def test_ok_truthy(self):
        self.assertTrue(self.ok)

    def test_err_falsy(self):
        self.assertFalse(self.err)
