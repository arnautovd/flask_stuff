import unittest
from app import app


class TestFlaskApp(unittest.TestCase):
    """Tests for the Flask application routes."""

    def setUp(self):
        """Set up test client before each test."""
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_hello_route(self):
        """Test the root route returns hello message."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, world')

    def test_get_sum_route(self):
        """Test the /get_sum route returns correct sum."""
        response = self.client.get('/get_sum')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '30')

    def test_hello_with_string_data(self):
        """Test the /hello/<string:data> route with normal data."""
        response = self.client.get('/hello/testdata')
        self.assertEqual(response.status_code, 200)
        # The template should render with the mutated data
        self.assertIn(b'The length of testdata is 8', response.data)

    def test_hello_with_censored_word(self):
        """Test the /hello/<string:data> route with censored word."""
        response = self.client.get('/hello/fuck')
        self.assertEqual(response.status_code, 200)
        # The template should render with CENSORED
        self.assertIn(b'CENSORED', response.data)


if __name__ == '__main__':
    unittest.main()
