import unittest
import name_function

class NamesTestCase(unittest.TestCase):
    """тест для name_function.py"""
    def test_first_last_name(self):
        form_name =name_function.get_formatted_name('janic','joplin')
        self.assertEquals(form_name,'Janic Joplin')
    def test_first_last_midlle_name(self):
        form_name =name_function.get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEquals(form_name,'Wolfgang Amadeus Mozart')



if __name__ == '__main__':
    unittest.main()


# print('Нажмите для выхода q')
# while True:
#     first = input('First name ')
#     if first == 'q':
#         break
#     last = input('Last name ')
#     if first == 'q':
#         break
#     form_name =
#     print(f"\tFormatted name {form_name}")