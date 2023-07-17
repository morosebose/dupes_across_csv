'''
uniques_across_csv.py

This program compares data in the specified column of each of two CSVs
and writes out a new CSV with the data unique to the second file.

Copyright © 2023 Surajit A. Bose
'''

import csv
import os

# Default output filename
OUTFILE = 'uniques.csv'


def getDataFromFile(first) :
    '''
    Get filename and file info from user.

    Parameters
    ----------
    first : bool
        If True, this is the first file.
        Else, it is the file to check for uniques.

    Returns
    -------
    filename : string
        Name of input file supplied by user
    data_set : set
        Set with the relevant data from the file
    '''  
    prompt = 'first' if first else 'second'
    data_set = set()
    
    # Get filename
    valid_file = False
    while not valid_file :
        filename = input(f'Enter filename of the {prompt} csv: ')
        if os.path.isfile(filename) :
                valid_file = True
        else :
            print("File not found. Please check the path and filename, and include the .csv suffix.\n")

    # Get column number
    valid_num = False
    while not valid_num : 
        num = input(f'Enter the index of the column in {filename} with the data to check: ')
        try :
            col = int(num)
            valid_num = True
        except ValueError :
            print ('Invalid number, please try again.')
    
    # Does file have header row?
    valid_head = False
    while not valid_head :
        has_header = input(f'Does {filename} have a header row? [y/n]: ')
        if has_header[0].lower() in ['y', 'n'] :
            valid_head = True
        else : 
            print('Invalid input, please try again.')
    header = True if has_header == 'y' else False
    
    # Get data from file and add to set
    with open (filename, 'r') as csvfile:
        csv_rows = csv.reader(csvfile)
        
        # Skips header row
        if header : 
            next(csv_rows)
        
        # Adds each elem to the set of known data
        for row in csv_rows:
            data_set.add(row[col]) 
    
    return (filename, data_set)


def writeUniqueData(first_file, first_data, second_file, second_data) : 
    '''
    Write out the data that is only in second file and not in first.
    
    Parameters
    ----------
    first_file : string
        Filename of first file.
    first_data : set
        Relevant data from first file.
    second_file : string
        Filename of second file.
    second_data : set
        Relevant data from second file.

    Raises
    ------
    SystemExit
        If unable to write to output file, quit with error message.

    Returns
    -------
    None.
    '''
    uniq_data = second_data.difference(first_data) # new_data - orig_data
    outfile = input(f'Enter filename to write unique data, or return for default {OUTFILE}: ')
    if not outfile :
        outfile = OUTFILE
    try :
        with open (outfile, 'w', newline = '') as fh :
            writefile = csv.writer(fh)
            writefile.writerow([f'Uniques in {second_file} not in {first_file}'])
            writefile.writerows([elem] for elem in uniq_data)        
        print(f'Unique data successfully written to {outfile}.\n')
    except IOError :
        raise SystemExit('Error writing output file')


def getUniqueData() :
    '''
    Code driver
    '''
    first_file, first_data = getDataFromFile(True)
    second_file, second_data = getDataFromFile(False)
    writeUniqueData(first_file, first_data, second_file, second_data) 


if __name__ == '__main__' :
    getUniqueData()
    
