
# A dummy test_harness for testing out CI configurations
import unittest

from dummy import hello

class BaseTestCase(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
