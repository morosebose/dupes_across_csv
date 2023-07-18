'''
uniques_across_csv.py

This program compares data in the specified column of each of two CSVs
and writes out a new CSV with the data unique to the second file.

Copyright © 2023 Surajit A. Bose
'''

import csv
import os

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
                fpath, fname = os.path.split(filename)
                valid_file = True
        else :
            print("File not found. Please check the path and filename, and include the .csv suffix.\n")

    # Get column number
    valid_num = False
    while not valid_num : 
        num = input(f'Enter the index of the column in {fname} with the data to check: ')
        try :
            col = int(num)
            valid_num = True
        except ValueError :
            print ('Invalid number, please try again.')
    
    # Does file have header row?
    valid_head = False
    while not valid_head :
        has_header = input(f'Does {fname} have a header row? [y/n]: ')[0].lower()
        if has_header in ['y', 'n'] :
            valid_head = True
        else : 
            print('Invalid input, please try again.')
    
    # Get data from file and add to set
    with open (filename, 'r') as csvfile:
        csv_rows = csv.reader(csvfile)
        
        # Skips header row
        if has_header == 'y' : 
            next(csv_rows)
        
        # Adds each elem to the set of known data
        for row in csv_rows:
            data_set.add(row[col]) 
    
    return (filename, data_set)    


def writeUniqueData(xfile, xdata, yfile, ydata) : 
    '''
    Write out the data that is only in second file and not in first.
    
    Parameters
    ----------
    xfile : string
        Filename of first file.
    xdata : set
        Relevant data from first file.
    yfile : string
        Filename of second file.
    ydata : set
        Relevant data from second file.

    Raises
    ------
    SystemExit
        If unable to write to output file, quit with error message.

    Returns
    -------
    None.
    '''
    uniq_data = ydata.difference(xdata) # new_data - orig_data
    xpath, xname = os.path.split(xfile)
    ypath, yname = os.path.split(yfile)
    
    print(f'\n*** NOTE: output file will be in same directory as {yname} ***\n')
    
    num = 1
    default = 'unique' + str(num) + '.csv'
    while os.path.isfile(os.path.join(ypath, default)) :
        num += 1
        default = 'unique' + str(num) + '.csv'
    
    valid_filename = False
    while not valid_filename :
        fname = input(f'Enter output filename, or return to use default {default}: ')
        fout = fname if fname else default
        outfile = os.path.join(ypath, fout) 
        if os.path.isfile(outfile) :
            print(f'{fout} already exists, please enter a unique filename.')
        else :
            valid_filename = True
        
    try :
        with open (outfile, 'w', newline = '') as fh :
            writefile = csv.writer(fh)
            writefile.writerow([f'Data in {yname} not in {xname}'])
            writefile.writerows([elem] for elem in uniq_data)        
        print(f'Unique data in {yname} successfully written to {fout}.\n')
    except IOError :
        raise SystemExit('Error writing output file')
        

def wantsViceVersa(first_file, first_data, second_file, second_data) :
    '''
    Check if user wants to write out unique data from first file too.
    If yes, write out the data that is only in first file and not in second.

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

    Returns
    -------
    None.
    '''
    xpath, xname = os.path.split(first_file)
    
    valid_want = False
    while not valid_want :
        wants_vice = input(f'Would you like a file with unique data in {xname}? [y/n]: ')[0].lower()
        if wants_vice in ['y', 'n'] :
            valid_want = True
        else : 
            print('Invalid input, please try again.')
    
    if wants_vice == 'y' :
        writeUniqueData(second_file, second_data, first_file, first_data)


def getUniqueData() :
    '''
    Code driver
    '''
    first_file, first_data = getDataFromFile(True)
    second_file, second_data = getDataFromFile(False)
    writeUniqueData(first_file, first_data, second_file, second_data) 
    wantsViceVersa(first_file, first_data, second_file, second_data)


if __name__ == '__main__' :
    getUniqueData()
    
