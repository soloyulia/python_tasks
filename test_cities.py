import city_function,unittest
class Cities_Names(unittest.TestCase):
    def test_cities(self):
        form_name = city_function.country_city('russian','moskow')
        self.assertEquals(form_name, 'Russian, Moskow')
    def test_cities_population(self):
        form_name = city_function.country_city('russian','moskow',5000)
        self.assertEquals(form_name,'Russian, Moskow, 5000')
if __name__ == '__main__':
    unittest.main()
