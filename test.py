import unittest
from helpers.helpersTest import HelpersTests
from FPGrowthNew.dbTreeTests import DBNodeTests
from FPGrowthNew.dbTreeTests import DBTreeTests

def suite():
    suite = unittest.TestSuite()
    suite.addTest(HelpersTests('testPreprocess'))

    suite.addTest(DBNodeTests('testAdd'))
    suite.addTest(DBNodeTests('testSearchChildren'))

    suite.addTest(DBTreeTests('testAddOneTransaction'))
    suite.addTest(DBTreeTests('testAddIndependentTransactions'))
    suite.addTest(DBTreeTests('testAddCommonPrefixes'))
    suite.addTest(DBTreeTests('testGetPaths'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
