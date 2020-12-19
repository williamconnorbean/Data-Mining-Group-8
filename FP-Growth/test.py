import sys
sys.path.append('../')

from fp_growth import find_frequent_itemsets, find_frequent_itemsets_1_tdb_scan
from FPGrowthNew import DBTree
import csv

transactions = []
dbTree = DBTree.DBTree()

# first tdb scan
with open("./test.csv") as database:
    for row in csv.reader(database):
        transactions.append(row)
        dbTree.add(row)

minsup = 3

# mine frequent itemsets using original FP-Growth
for itemset in find_frequent_itemsets(transactions, minsup, "./test.csv", True):
    print itemset

print

# mine frequent itemsets using New FP-Growth with DBTree
for itemset in find_frequent_itemsets_1_tdb_scan(dbTree, minsup):
    print itemset
