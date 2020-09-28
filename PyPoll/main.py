import os
import csv

csvpath = os.path.join('/Users/jameswilliams/Desktop/GT_Data_Boot_Camp/GT_Homework/python-challenge/PyBank/Resources/JamesWilliams_election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

