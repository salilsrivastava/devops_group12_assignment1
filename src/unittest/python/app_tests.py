import unittest
from main.python.app import app

class app_tests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_nonexistent_route(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_convert_epoch_to_datetime(self):
        epoch_time = 1710009507
        response = self.app.get(f'/convert_epoch?epoch_time={epoch_time}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Converted Datetime:</h1>', response.data)
        self.assertIn(b'2024-03-09 18:38:27', response.data)

    def test_invalid_epoch_parameter(self):
        epoch_time = 'invalid_epoch'
        response = self.app.get(f'/convert_epoch?epoch_time={epoch_time}')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'<h1>Error:', response.data)

    def test_missing_epoch_parameter(self):
        response = self.app.get('/convert_epoch')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'<h1>Error: Epoch time parameter is required.</h1>', response.data)

if __name__ == '__main__':
    unittest.main()