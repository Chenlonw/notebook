# -*- coding: utf-8 -*-
import unittest

class absTest(unittest.TestCase):
    """定义单元测试组"""
    def setUp(self):
        print 'set up for essential env'

    def tearDown(self):
        print 'close env'

    def testPositive(self):
        print 'test positive'
        self.assertEquals(abs(1), 1)

    def testNegative(self):
        print 'test negative'
        self.assertNotEquals(abs(-1), -1)

    def testTrue(self):
        print 'test true'
        self.assertTrue(abs(-1))

    def testType(self):
        print 'test type'
        with self.assertRaises(TypeError):
            abs({})

def abs_suite():
    suite = unittest.TestSuite()
    suite.addTest(absTest)
    return suite

if __name__ == '__main__':
    # unittest.main()
    suite = abs_suite()
    unittest.TextTestRunner(verbosity=2).run(suite)
