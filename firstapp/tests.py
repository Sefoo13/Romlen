import unittest
import testcase
# from firstapp.testcase import add, sub

class CalcBasicTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(testcase.add(1,2),3)

    def test_sub(self):
        self.assertEqual(testcase.sub(4,2),2)

if __name__ == '__main__':
    unittest.main()
