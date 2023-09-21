import unittest
from main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_data(self):
        response = self.app.get('/get_data')
        data = response.get_data(as_text=True)
        expected_data = '{"Name": "Bhanuprakash N R", "Employee No": "12310"}'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
