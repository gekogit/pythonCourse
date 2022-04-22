import unittest
from fields import rectangle, triangle


class FieldsTestCase(unittest.TestCase):

    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(100, 5), 500)

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(6, 4), 12)


if __name__ == '__main__':
    unittest.main()