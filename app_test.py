import unittest
import app as app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.asserIn(b'Germinare',response.data)

if __name__ == '__main__':
    unittest.main()
