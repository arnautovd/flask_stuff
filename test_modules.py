import unittest
from modules import getSum, mutateData


class TestGetSum(unittest.TestCase):
    """Tests for the getSum function."""

    def test_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(getSum(10, 20), 30)

    def test_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(getSum(-5, -3), -8)

    def test_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        self.assertEqual(getSum(-5, 10), 5)

    def test_zeros(self):
        """Test adding zeros."""
        self.assertEqual(getSum(0, 0), 0)

    def test_floats(self):
        """Test adding floating point numbers."""
        self.assertEqual(getSum(1.5, 2.5), 4.0)


class TestMutateData(unittest.TestCase):
    """Tests for the mutateData function."""

    def test_censored_word_fuck(self):
        """Test that 'fuck' is censored."""
        self.assertEqual(mutateData('fuck'), 'CENSORED')

    def test_censored_word_suck(self):
        """Test that 'suck' is censored."""
        self.assertEqual(mutateData('suck'), 'CENSORED')

    def test_normal_word(self):
        """Test normal word returns formatted string with length."""
        result = mutateData('hello')
        self.assertEqual(result, 'The length of hello is 5')

    def test_empty_string(self):
        """Test empty string returns formatted string with length 0."""
        result = mutateData('')
        self.assertEqual(result, 'The length of  is 0')

    def test_single_character(self):
        """Test single character string."""
        result = mutateData('a')
        self.assertEqual(result, 'The length of a is 1')

    def test_sentence(self):
        """Test sentence returns formatted string with correct length."""
        result = mutateData('hello world')
        self.assertEqual(result, 'The length of hello world is 11')


if __name__ == '__main__':
    unittest.main()
