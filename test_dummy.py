# A dummy test_harness for testing out CI configurations
import logging
import unittest

from dummy import hello

logger = logging.getLogger('test_dummy')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        logger.debug('Set up for %s', self._testMethodName)

    def tearDown(self):
        logger.debug('Tear down for %s', self._testMethodName)

    def test_hello(self):
        self.assertEqual(hello(), 'Hello, world!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='test_dummy.log',
                        filemode='w', format='%(name)-10s %(message)s')
    unittest.main()
