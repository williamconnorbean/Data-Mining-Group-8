import csv

def preprocess(filepath):
    transactions = []

    with open(filepath) as database:
        for row in csv.reader(database):
            transactions.append(row)
    
    return transactions
