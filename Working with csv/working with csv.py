#Read a CSV file line by line with header


from csv import reader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)
        
        
#Read csv file without header

from csv import reader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            print(row)
            
            
            
#Read csv file line by line using csv module DictReader object

from csv import DictReader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        print(row)
        
#Get column names from header in csv file

from csv import DictReader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    column_names = csv_dict_reader.fieldnames
    print(column_names)
    
    
#Read specific columns (by column name) in a csv file while iterating row by row


from csv import DictReader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        print(row['Start'], row['End'])
        
        
#Read specific columns (by column Number) in a csv file while iterating row by row

from csv import reader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row[0], row[1])
        
        
        
        
#Import csv to a list of lists

from csv import reader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    print(list_of_rows)
    
    
#Select specific value in csv by specific row and column number

from csv import reader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    print(list_of_rows)

    row_number = 3
    col_number = 4
    value = list_of_rows[row_number - 1][col_number - 1]
    print('Value in cell at 3rd row and 4nd column : ', value)
    
    
    
#Use Pandas to read csv into a list of lists without header

import pandas as pd
df = pd.read_csv('d:\python\Chr.csv', delimiter=',')
list_of_rows = [list(row) for row in df.values]
print(list_of_rows)


#Use Pandas to read csv into a list of lists with header

import pandas as pd
df = pd.read_csv('d:\python\Chr.csv', delimiter=',')
list_of_rows = [list(row) for row in df.values]
list_of_rows.insert(0, df.columns.to_list())
print(list_of_rows)

#Read csv into list of tuples

from csv import reader
with open('d:\python\Chr.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_tuples = list(map(tuple, csv_reader))
    print(list_of_tuples)
    
    
#Read csv into list of tuples using pandas & list comprehension

import pandas as pd
df = pd.read_csv('d:\python\Chr.csv', delimiter=',')
list_of_tuples = [tuple(row) for row in df.values]
print(list_of_tuples)


#Read csv into list of dictionaries

from csv import DictReader
with open('d:\python\Chr.csv', 'r') as read_obj:
    dict_reader = DictReader(read_obj)
    list_of_dict = list(dict_reader)
    print(list_of_dict)
    
    
