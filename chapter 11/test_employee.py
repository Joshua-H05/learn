import unittest
from employee import Employee


class TestEmployees(unittest.TestCase):

    def setUp(self):
        self.joshua_hu = Employee("Joshua", "Hu", 40_000)
        self.salary_raise = [5_000, 10_000]

    def test_default_raise(self):
        self.joshua_hu.give_raise()
        self.assertEqual(self.joshua_hu.salary, 45_000)

    def test_custom_raise(self):
        self.joshua_hu.give_raise(self.salary_raise[1])
        self.assertEqual(self.joshua_hu.salary, 50_000)


if __name__ == "__main__":
    unittest.main()
