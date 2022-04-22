import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_emai(self):
        obj_anna = Student('ana', 'kowalska', 4.6, None)

        self.assertEqual(obj_anna.email, 'ana.kowalska@university.com')

        obj_anna.name = 'anna'
        self.assertEqual(obj_anna.email, 'anna.kowalska@university.com')


if __name__ == '__main__':
    unittest.main()