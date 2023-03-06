import unittest

from quick_test_file import country_info

class TestCountryName(unittest.TestCase):
    """Tests to see if the function 'country_info' works properly"""

    def test_city_country(self):
        """Verifies that a string is printed in the right format"""
        formatted_city = country_info('lagos','nigeria')
        self.assertEqual(formatted_city,'Lagos, Nigeria')

    def test_city_country_population(self):
        """Verifies that our function includes population"""
        formatted_city = country_info('lagos','nigeria',10000)
        self.assertEqual(formatted_city,'Lagos, Nigeria - population: 10000')

unittest.main()

