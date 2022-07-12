import unittest
from city_functions import describe_location


class LocationTestCase(unittest.TestCase):

    def test_city_country(self):
        location_info = describe_location("shanghai", "china")
        self.assertEqual(location_info, "Shanghai, China")


if __name__ == "main":
    unittest.main()

