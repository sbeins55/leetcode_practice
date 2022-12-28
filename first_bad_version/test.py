import unittest

from first_bad_version.solution import first_bad_version


def generator(bad_version):
    def is_bad_version(version):
        return version >= bad_version

    return is_bad_version


class FirstBadVersionTest(unittest.TestCase):

    def test_one_element(self):
        expected = 1
        actual = first_bad_version(1, generator(expected))
        self.assertEqual(expected, actual)

    def test_odd_elements(self):
        expected = 15
        actual = first_bad_version(21, generator(expected))
        self.assertEqual(expected, actual)

    def test_even_elements(self):
        expected = 1200
        actual = first_bad_version(1500, generator(expected))
        self.assertEqual(expected, actual)
