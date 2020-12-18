import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.getcwd()))+'/FP-Growth')

from fp_growth import find_frequent_itemsets
import csv


age_gourps = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80']
prov = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Nova Scotia', 'Nunavut', 'NL', 'PEI', 'Ontario', 'Quebec', 'Saskatchewan', 'Yukon']
gender = ['Male', 'Female']

transactions = []
with open("../../data/canada-covid-details-reduced.csv") as database:
    for row in csv.reader(database):
        transactions.append(row)

minsup = 10
for itemset in find_frequent_itemsets(transactions, minsup, True):
    if(len(itemset[0]) == 3 and 
        (
            (list(itemset[0])[0] in gender and list(itemset[0])[1] in age_gourps and list(itemset[0])[2] in prov) or
            (list(itemset[0])[0] in gender and list(itemset[0])[1] in prov and list(itemset[0])[2] in age_gourps) or
            (list(itemset[0])[0] in age_gourps and list(itemset[0])[1] in prov and list(itemset[0])[2] in gender) or 
            (list(itemset[0])[0] in age_gourps and list(itemset[0])[1] in gender and list(itemset[0])[2] in prov) or 
            (list(itemset[0])[0] in prov and list(itemset[0])[1] in age_gourps and list(itemset[0])[2] in gender) or
            (list(itemset[0])[0] in prov and list(itemset[0])[1] in gender and list(itemset[0])[2] in age_gourps)
        )):
        print itemset

