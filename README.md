# Data-Mining-Group-8

## Mining Section

### Province

The python code for mining the most vulnerable age-group in each provience in Canada with and without gender can be found in *mining/province/vulnerable_group_with_new_FP.py* and *mining/province/vulnerable_group.py*.

To run *vulnerable_group_with_new_FP.py*:

**NOTE: This python file is using the new FP_growth method to find the result.**

1. *python vulnerable_group_with_new_FP.py ALL > prov.csv* This will output a table contain the count for each age_group in each province from our database.
2. *python vulnerable_group_with_new_FP.py GENDER > prov_gender.csv* This will output a table contain the coutn for males and females of each age_group in each province from our database.

To run *vulnerable_group.py*:

**NOTE: this python file is using the old FP_growth method to find the result.**

1. *python vulnerable_group.py ALL > old_prov.csv* This will output a table contain the count for each age_group in each province from our database.
2. *python vulnerable_group.py GENDER > old_prov_gender.csv* This will output a table contain the count for males and females of each age_group in each province from our database.

### Time

The python code for mining the most vulnerable age-gender group in each month in Canada can be found in *mining/time/timeMining.py* and *mining/time/timeMiningUsingNewFP.py*.

To run *timeMiningUsingNewFP.py*:

**NOTE: This python file is using the new FP_growth method to find the result.**

1. *python timeMiningUsingNewFP.py* will output the total number of transactions and the age-gender group with largest support in percentage for each month and the entire time range mining from the entire database `canada-covid-details-reduced.csv`.

To run *timeMining.py*:

**NOTE: this python file is using the old FP_growth method to find the result.**

1. *python timeMining.py* will output the total number of transactions and the age-gender group with largest support in percentage for each month and the entire time range mining from the entire database `canada-covid-details-reduced.csv`.

## Unit Tests
Our modification to the original FP-Growth algorithm comes with a suite of unit tests to ensure code quality. The tests cover the creation of the REP-Tree as well as the functions that each node of the REP-Tree are responsible for.

To execute the unit tests:
1. Map to the root of the project directory
2. Run `python test.py`
