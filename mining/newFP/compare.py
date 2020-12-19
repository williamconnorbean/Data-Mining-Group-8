import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.getcwd()))+'/FP-Growth')
sys.path.append('../../')

from fp_growth import find_frequent_itemsets, find_frequent_itemsets_1_tdb_scan
from FPGrowthNew import DBTree
import csv
import time

minsup = 3

transactions = []
start1 = time.time()

# first tdb scan
with open("../../data/canada-covid-details-reduced.csv") as database:
    for row in csv.reader(database):
        transactions.append(row)
print "Num of transaction: %d " %  len(transactions)
print "Num of items: %d " %  len(transactions[0])
end1 = time.time()
print "FP Growth"
print "Time for 1st db scan: %f " %  (end1 - start1)
start2 = time.time()
# mine frequent itemsets using original FP-Growth with second scan
find_frequent_itemsets(transactions, minsup, "../../data/canada-covid-details-reduced.csv", True)
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
find_frequent_itemsets_1_tdb_scan(dbTree, minsup)
end2 = time.time()
print "Time for mining without 2nd DB scan : %f " %  (end2 - start2)
print "Total time : %f " %  (end2 - start1)

