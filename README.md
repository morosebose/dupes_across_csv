# Uniques Across CSVs

## Description
Given two CSV files, each with a column containing the same kind of data:

- This script outputs a third CSV file that includes only the data from the second CSV that isn't in the first
- It the user wants, the script outputs a fourth CSV file that includes only the data from the first CSV that isn't in the second.

For example, if:

- `foo.csv` has a column `tel_nos` with phone numbers of contacts
- `bar.csv` has a column `telephone` with phone numbers of contacts

The script will compare the two columns and:

- write out a file of all the telephone numbers in `bar.csv telephone` that are not in `foo.csv tel_nos`
- optionally, write out a file of all the telephone numbers in `foo.csv tel_nos` that are not in `bar.csv telephone`. 

## Credits
- This script is part of the Name Filtering Tools project of [They See Blue](https://www.theyseeblue.org/)
- Copyright Surajit A. Bose © 2023.
