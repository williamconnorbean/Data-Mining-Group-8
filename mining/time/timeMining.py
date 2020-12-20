import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.getcwd()))+'/FP-Growth')
sys.path.append('../../')

from fp_growth import find_frequent_itemsets
import csv
import datetime

NUM_MONTH = 12

transactions = []
for i in range(NUM_MONTH + 1):
    transactions_monthly = []
    transactions.append(transactions_monthly)

with open("../../data/canada-covid-details-reduced.csv") as database:
    for row in csv.reader(database):
        date_time_str = row[0]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y/%m/%d %H:%M:%S')
        transactions[date_time_obj.month-1].append(row[2:4])
        transactions[NUM_MONTH].append(row[2:4])

minsup = 0.05
for i in range(NUM_MONTH + 1):
    if i == 12:
        print("\n\nEntire time range:")
    else:
        print("\n\nMonth #{}:".format(i+1))
    print("Total transactions: {}\n".format(len(transactions[i])))
    print("-------------------------------")

    maxCount = 0
    frequentItem = None

    for itemset, support in find_frequent_itemsets(transactions[i], minsup, "../../data/canada-covid-details-reduced.csv", True, True):
        if len(itemset) == 2 and 'Not Reported' not in itemset:
            if support > maxCount:
                maxCount = support
                frequentItem = itemset
    maxSupport = 0
    if len(transactions[i]) != 0:
        maxSupport = (float(maxCount)/float(len(transactions[i]))) * 100
    print("{0}, support {1:.2f}%".format(frequentItem, maxSupport))