from fp_growth import find_frequent_itemsets
import csv

transactions = []

# first tdb scan
with open("./test.csv") as database:
    for row in csv.reader(database):
        transactions.append(row)

minsup = 2
for itemset in find_frequent_itemsets(transactions, minsup, "./test.csv", True):
    print itemset
