import unittest
import helpers

class HelpersTests(unittest.TestCase):
    def testPreprocess(self):        
        fileName = "helpers/test.csv"
        transactions = helpers.preprocess(fileName)
        
        result = [
            ['9/9/2020 12:00','Region of Waterloo, Public Health','50-59','Female','Close Contact','Recovered','Ontario'],
            ['11/4/2020 12:00','Peel Public Health','20-29','Female','Close Contact','Active','Ontario'],
            ['10/25/2020 12:00','Peel Public Health','40-49','Male','Close Contact','Recovered','Ontario'],
            ['10/14/2020 12:00','Peterborough Public Health','<20','Female','Not Reported','Recovered','Ontario'],
            ['9/18/2020 12:00','Region of Waterloo, Public Health','50-59','Male','Not Reported','Recovered','Ontario']
        ]

        self.assertEqual(len(transactions), 5)
        self.assertEqual(transactions, result)