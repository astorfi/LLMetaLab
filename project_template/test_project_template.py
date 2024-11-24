import unittest
from main import example_function

class TestExampleFunction(unittest.TestCase):
    def test_output(self):
        self.assertEqual(example_function(5), 10)

if __name__ == '__main__':
    unittest.main()
