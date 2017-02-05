
from scriptcore.encoding.encoding import Encoding
import os
import tempfile
import unittest
import shutil
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import sys
import random
import string


class TestCase(unittest.TestCase):

    def set_up(self):
        """
        Set up the test case
        """

        self._temp_files = []
        self._temp_dirs = []

        self.stdout_original = sys.stdout
        sys.stdout = self.stdout = StringIO()
        self.stderr_original = sys.stderr
        sys.stderr = self.stderr = StringIO()
        self.stdin_original = sys.stdin
        sys.stdin = self.stdin = StringIO()

    def tear_down(self):
        """
        Tear down the test case
        """

        for temp_file in self._temp_files:
            if os.path.isfile(temp_file):
                os.remove(temp_file)
        for temp_dir in self._temp_dirs:
            if os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)

        sys.stdout = self.stdout_original
        sys.stderr = self.stderr_original
        sys.stdin = self.stdin_original

    def temp_file(self, only_path=False, suffix='', prefix='tmp'):
        """
        Get temp file
        :param only_path:   Only return the path
        :param suffix:      File suffix
        :param prefix:      File prefix
        :return:            Path to temp file
        """

        path = tempfile.mktemp(suffix=suffix, prefix=prefix)
        if only_path and os.path.isfile(path):
            os.remove(path)
        self._temp_files.append(path)
        return path

    def write_temp_file(self, content, suffix='', prefix='tmp'):
        """
        Write to temp file
        :param content: The content to write to file
        :param suffix:  File suffix
        :param prefix:  File prefix
        :return:        The file path
        """

        path = self.temp_file(suffix=suffix, prefix=prefix)

        with open(path, 'w') as file:
            file.write(content)

        return path

    def temp_dir(self, only_path=False, suffix='', prefix='tmp'):
        """
        Get temp dir
        :param only_path:   Only return the path
        :param suffix:      File suffix
        :param prefix:      File prefix
        :return:            Path to temp dir
        """

        path = tempfile.mkdtemp(suffix=suffix, prefix=prefix)
        if only_path and os.path.isdir(path):
            shutil.rmtree(path)
        self._temp_dirs.append(path)
        return path

    def tests_dir(self):
        """
        Get the tests directory
        :return:    Directory
        """

        current_dir = os.path.dirname(os.path.abspath(__file__))
        tests_dir = os.path.join(current_dir, '../../tests')
        tests_dir = os.path.abspath(tests_dir)
        return tests_dir

    def rand_str(self, length=20):
        """
        Get random string of certain length
        :param length:  The length of the string
        :return:        Random string
        """

        return Encoding.normalize(''.join(random.choice(string.ascii_lowercase) for i in range(length)))

    def setUp(self):
        """
        Set up the test case
        """
        self.set_up()

    def tearDown(self):
        """
        Tear down the test case
        """
        self.tear_down()

    def assert_equal(self, a, b):
        """
        a == b
        """
        return self.assertEqual(a, b)

    def assert_not_equal(self, a, b):
        """
        a != b
        """
        return self.assertNotEqual(a, b)

    def assert_true(self, x):
        """
        bool(x) is True
        """
        return self.assertTrue(x)

    def assert_false(self, x):
        """
        bool(x) is False
        """
        return self.assertFalse(x)

    def assert_is(self, a, b):
        """
        a is b
        """
        return self.assertIs(a, b)

    def assert_is_not(self, a, b):
        """
        a is not b
        """
        return self.assertIsNot(a, b)

    def assert_is_none(self, x):
        """
        x is None
        """
        return self.assertIsNone(x)

    def assert_is_not_none(self, x):
        """
        x is not None
        """
        return self.assertIsNotNone(x)

    def assert_in(self, a, b):
        """
        a in b
        """
        return self.assertIn(a, b)

    def assert_not_in(self, a, b):
        """
        a not in b
        """
        return self.assertNotIn(a, b)

    def assert_is_instance(self, a, b):
        """
        isinstance(a, b)
        """
        return self.assertIsInstance(a, b)

    def assert_not_is_instance(self, a, b):
        """
        not isinstance(a, b)
        """
        return self.assertNotIsInstance(a, b)

    def assert_raises(self, exc, *args, **kwds):
        """
        fun(*args, **kwds) raises exc
        """
        return self.assertRaises(exc, *args, **kwds)

    def assert_raises_regexp(self, exc, r, *args, **kwds):
        """
        fun(*args, **kwds) raises exc and the message matches regex r
        """
        return self.assertRaisesRegexp(exc, r, *args, **kwds)

    def assert_almost_equal(self, a, b):
        """
        round(a-b, 7) == 0
        """
        return self.assertAlmostEqual(a, b)

    def assert_not_almost_equal(self, a, b):
        """
        round(a-b, 7) != 0
        """
        return self.assertNotAlmostEqual(a, b)

    def assert_greater(self, a, b):
        """
        a > b
        """
        return self.assertGreater(a, b)

    def assert_greater_equal(self, a, b):
        """
        a >= b
        """
        return self.assertGreaterEqual(a, b)

    def assert_less(self, a, b):
        """
        a < b
        """
        return self.assertLess(a, b)

    def assert_less_equal(self, a, b):
        """
        a <= b
        """
        return self.assertLessEqual(a, b)

    def assert_regexp_matches(self, s, r):
        """
        r.search(s)
        """
        return self.assertRegexpMatches(s, r)

    def assert_not_regexp_matches(self, s, r):
        """
        not r.search(s)
        """
        return self.assertNotRegexpMatches(s, r)

    def assert_items_equal(self, a, b):
        """
        sorted(a) == sorted(b) and works with unhashable objs
        """
        return self.assertItemsEqual(a, b)

    def assert_dict_contains_subset(self, a, b):
        """
        all the key/value pairs in a exist in b
        """
        return self.assertDictContainsSubset(a, b)

    def assert_multi_line_equal(self, a, b):
        """
        strings
        """
        return self.assertMultiLineEqual(a, b)

    def assert_sequence_equal(self, a, b):
        """
        sequences
        """
        return self.assertSequenceEqual(a, b)

    def assert_list_equal(self, a, b):
        """
        lists
        """
        return self.assertListEqual(a, b)

    def assert_tuple_equal(self, a, b):
        """
        tuples
        """
        return self.assertTupleEqual(a, b)

    def assert_set_equal(self, a, b):
        """
        sets or frozensets
        """
        return self.assertSetEqual(a, b)

    def assert_dict_equal(self, a, b):
        """
        dicts
        """
        return self.assertDictEqual(a, b)

    @unittest.skip
    def skip_test(self, reason):
        """
        Skip this test
        """
        return self.skipTest(reason)

    def assert_equal_deep(self, expected, value, check_type=True):
        """
        Assert equal deep
        :param expected:    The expected value
        :param value:       The value
        :param check_type:  Do type check
        :return:
        """

        if isinstance(expected, dict):
            self.assert_is_instance(value, dict)

            for i in range(0, len(expected)):
                self.assert_equal_deep(sorted(expected)[i], sorted(value)[i], check_type=check_type)
                self.assert_equal_deep(expected[sorted(expected)[i]], value[sorted(value)[i]], check_type=check_type)

        elif isinstance(expected, list):
            self.assert_is_instance(value, list)

            for i in range(0, len(expected)):
                self.assert_equal_deep(expected[i], value[i], check_type=check_type)

        else:
            self.assert_equal(expected, value)
            if check_type:
                self.assert_is_instance(value, type(expected))
