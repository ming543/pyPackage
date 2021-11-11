from showbox import showbox
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_add(self):
        self.assertTrue(showbox().textbox('Please link loopback cable of 485'))

    def tearDown(self):
        print("test end")

if __name__ ==  '__main__':
    unittest.main()

