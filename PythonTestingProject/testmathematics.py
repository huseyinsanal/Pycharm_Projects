import unittest


class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(10, 5)  # add assertion here

    def test_second(self):
        self.assertEqual(10, 5)

if __name__ == '__main__':
    unittest.main()
