import sys
sys.path.append('../')

from fp_growth import find_frequent_itemsets, find_frequent_itemsets_1_tdb_scan
from FPGrowthNew import DBTree
import csv

transactions = []
dbTree = DBTree.DBTree()

# first tdb scan
with open("../data/canada-covid-details-reduced.csv") as database:
    for row in csv.reader(database):
        transactions.append(row)
        dbTree.add(row)

minsup = 0.5

print "FP Growth"

# mine frequent itemsets using original FP-Growth
for itemset, count in find_frequent_itemsets(transactions, minsup, "../data/canada-covid-details-reduced.csv", True, True):
    print itemset, count

print "\nNew FP Growth"

# mine frequent itemsets using New FP-Growth with DBTree
for itemset, count in find_frequent_itemsets_1_tdb_scan(dbTree, minsup, True):
    print itemset, count
