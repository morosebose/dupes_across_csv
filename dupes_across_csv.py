# Script for checking whether a given name is already in TSB's database, and adding it to an output file if not

# Read in csv of names already in database and create a set. 
# Assumptions: 
#    Names already known are in tsb_names.csv
#    Names to check are in check_names.csv
#    New names are written to additional_names.csv
#    Single column
#    One name per row 
#    Header row

import csv

# Create empty sets to hold the known and new names
known_names = set()
new_names = set()

# Read file of names already in database
# Add each name therein to set of known names
with open ('tsb_names.csv', 'r') as csvfile:
    csv_rows = csv.reader(csvfile)
    
    # Skips header row
    csv_rows.next()
    
    # Adds each name to the set of known names
    for row in csv_rows:
        known_names.add(row[0]) 
    
# Read file of potentially new names
# Add each new name to set of new names
with open ('check_names.csv', 'r') as csvfile:
    csv_rows = csv.reader(csvfile)
    
    # Skips header row
    csv_rows.next()
    
    # Adds each name to the set of known names
    for row in csv_rows:
        if row[0] not in set(known_names):
            new_names.add(row[0]) 
    for elem in set(new_names):
        print(elem)


    
# Write new names to csv 
# This doesn't work as it treats each character as a separate field in each row.
'''
with open ('additional_names.csv', 'w') as writefile:
    written_file = csv.writer(writefile)
    written_file.writerows(set(new_names))
'''

# Have to use DictWriter instead

with open ('additional_names.csv', 'w') as writefile:
    written_file = csv.DictWriter(writefile, fieldnames = {'Name'})
    written_file.writeheader()
    for elem in set(new_names):
        written_file.writerow({'Name' : elem })
