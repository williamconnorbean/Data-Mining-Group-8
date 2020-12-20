import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.getcwd()))+'/FP-Growth')
sys.path.append('../../')

from fp_growth import find_frequent_itemsets, find_frequent_itemsets_1_tdb_scan
from FPGrowthNew import DBTree
import csv
import time

directory = "../../data/differentDB"
minsup = 0.1
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        print filename
        print "-----------------------------------------"
        transactions = []
        start1 = time.time()

        # first tdb scan
        with open(directory+"/"+filename) as database:
            for row in csv.reader(database):
                transactions.append(row)
        print "Num of transaction: %d " %  len(transactions)
        print "Num of items: %d " %  len(transactions[0])
        end1 = time.time()
        print "\n\nFP Growth"
        print "Time for 1st db scan: %f " %  (end1 - start1)

        start2 = time.time()
        # mine frequent itemsets using original FP-Growth with second scan
        for itemset, support in find_frequent_itemsets(transactions, minsup, directory+"/"+filename, True, True):
            pass

        end2 = time.time()

        print "Time for mining with 2nd DB scan : %f " %  (end2 - start2)
        print "Total time : %f " %  (end2 - start1)

        dbTree = DBTree.DBTree()
        start1 = time.time()
        # first tdb scan
        with open("../../data/canada-covid-details-reduced.csv") as database:
            for row in csv.reader(database):
                dbTree.add(row)
        end1 = time.time()
        print "\n\nNew FP Growth"
        print "Time for 1st db scan: %f " %  (end1 - start1)
        start2 = time.time()

        # mine frequent itemsets using New FP-Growth with DBTree with second scan
        for itemset, support in find_frequent_itemsets_1_tdb_scan(dbTree, minsup, True):
            pass

        end2 = time.time()
        print "Time for mining without 2nd DB scan : %f " %  (end2 - start2)
        print "Total time : %f \n\n" %  (end2 - start1)
