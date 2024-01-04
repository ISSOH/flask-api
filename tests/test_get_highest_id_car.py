import unittest

from application import get_highest_id_car


class TestApi(unittest.TestCase):
    cars = [
        {
            'id': 5,
            'manufacturer': 'Ford',
            'model': 'Ford Bronco',
            'build': '1958'
        },
        {
            'id': 2,
            'manufacturer': 'Tesla',
            'model': 'T 258',
            'build': '2019'
        },
        {
            'id': 4,
            'manufacturer': 'Volvo',
            'model': 'Volvo C40',
            'build': '2000'
        }
    ]

    def test_highest_id_car(self):
        expected_id = 5
        highest_id_car = get_highest_id_car(self.cars)
        self.assertEqual(expected_id, highest_id_car)


if __name__ == '__main__':
    unittest.main()