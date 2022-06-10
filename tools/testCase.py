#python3
import unittest
import foo

class addTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (100, 99)

    def tearDown(self):
        self.args = None

    def testAdd(self):
        expected = 19;
        result = foo.addInt(*self.args);
        self.assertEqual(expected, result);

suite = unittest.TestSuite()
suite.addTest(addTestCase('testAdd'))

unittest.TextTestRunner(verbosity=2).run(suite)


