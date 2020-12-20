import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.getcwd()))+'/FP-Growth')
sys.path.append('../../')

from fp_growth import find_frequent_itemsets, find_frequent_itemsets_1_tdb_scan
from FPGrowthNew import DBTree
import csv

age_gourps = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80']
prov = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Nova Scotia', 'Nunavut', 'NL', 'PEI', 'Ontario', 'Quebec', 'Saskatchewan', 'Yukon']
gender = ['Male', 'Female']

dbTree = DBTree.DBTree()
with open("../../data/canada-covid-details-reduced.csv") as database:
    for row in csv.reader(database):
        tran = row[2:4]
        tran.append(row[6])
        # print tran
        dbTree.add(tran)






results = []
if str(sys.argv[1]) == "ALL":
    minsup = 10
    for itemset, count in find_frequent_itemsets_1_tdb_scan(dbTree, minsup, True):
        # print itemset, count
        if(len(itemset) == 2 and (itemset[0] in age_gourps and itemset[1] in prov)):
            results.append([itemset[1], itemset[0], count])
        elif ( len(itemset) == 2 and  (itemset[0] in prov and itemset[1] in age_gourps)):
            itemset.append(count)
            results.append(itemset)
    for item in prov:
        temp = []
        for result in results:
            if(result[0] == item):
                temp.insert(0, result)
            else:
                temp.append(result)
        results = temp
    
    temp = ''
    for result in results:
        if(result[0] != temp):
            print ["Prov", "Age Group", "Count"]
        temp = result[0]
        print result

else:
    minsup = 10
    for itemset, count in find_frequent_itemsets_1_tdb_scan(dbTree, minsup, True):
        if(len(itemset) == 3 and (itemset[0] in gender and itemset[1] in age_gourps and itemset[2] in prov) ):
            results.append([itemset[2], itemset[0], itemset[1], count])
        elif(len(itemset) == 3 and (itemset[0] in gender and itemset[1] in prov and itemset[2] in age_gourps) ):
            results.append([itemset[1], itemset[0], itemset[2], count])
        elif(len(itemset) == 3 and (itemset[0] in age_gourps and itemset[1] in prov and itemset[2] in gender) ):
            results.append([itemset[1], itemset[2], itemset[0], count])
        elif(len(itemset) == 3 and (itemset[0] in age_gourps and itemset[1] in gender and itemset[2] in prov) ):
            results.append([itemset[2], itemset[1], itemset[0], count])
        elif(len(itemset) == 3 and (itemset[0] in prov and itemset[1] in age_gourps and itemset[2] in gender) ):
            results.append([itemset[0], itemset[2], itemset[1], count])
        elif(len(itemset) == 3 and (itemset[0] in prov and itemset[1] in gender and itemset[2] in age_gourps) ):
            results.append([itemset[0], itemset[1], itemset[2], count])
    
    for item in prov:
        temp = []
        for result in results:
            if(result[0] == item):
                temp.insert(0, result)
            else:
                temp.append(result)
        results = temp
    
    for item in gender:
        temp = []
        for result in results:
            if(result[1] == item):
                temp.insert(0, result)
            else:
                temp.append(result)
        results = temp
        
    temp = ''
    for result in results:
        if(result[0] != temp):
            print ["Prov", "Gender", "Age Group", "Count"]
        temp = result[0]
        print result
