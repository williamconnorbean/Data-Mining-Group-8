import unittest
from helpers.helpersTest import HelpersTests

def suite():
    suite = unittest.TestSuite()
    suite.addTest(HelpersTests('testPreprocess'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
