"""
cse6242 s21
wrangling.py - utilities to supply data to the templates.

This file contains a pair of functions for retrieving and manipulating data
that will be supplied to the template for generating the table. """
import csv

def username():
    return 'atorres78'

def data_wrangling():
    with open('data/movies.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        table = list()
        # Feel free to add any additional variables
        n_lines = 0
        
        # Read in the header
        for header in reader:
            break
        
        # Read in each row
        for row in reader:
            if n_lines >= 100:
                break
            n_lines +=1 
            table.append(row)
            
        # Order table by the last column - [3 points] Q5.b
        newTable = sorted(table, key=lambda item: float(item[2]), reverse=True)
    
    return header, newTable

