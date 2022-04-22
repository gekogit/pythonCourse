import unittest
from fields import rectangle, triangle


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 50

    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(self.a, self.b), 500)

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(self.a, self.b), 250)

    def tearDown(self):
        del self.a
        del self.b


if __name__ == '__main__':
    unittest.main()