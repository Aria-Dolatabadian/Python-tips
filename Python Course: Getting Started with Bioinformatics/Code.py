import numpy as np
import pandas as pd
#load data into the object "df" using the pandas "read_table" function
df1 = pd.read_table('filename.txt', sep="\t", header=0)
print(df1)
print(df1.dtypes)
# Import an excel spreadsheet using pandas
df2 = pd.read_excel('filename.xlsx')
print(df2)
print(df2.dtypes)
#import a .csv dataset using numpy
df3 = pd.read_csv('filename.csv', sep=';')
print(df3)
print(df3.dtypes)

# define our function named as seq_length
def seq_length(seq):
    counter = 0
    while seq[counter:]:
        counter += 1
    return counter #returns the sequence length


# Execute our function, print length of given sequence
seq1 = "ATCTGGCAATGC"
print(seq_length(seq1))

#Visualisation

#import packages
import pandas as pd
import numpy as np
#Read the dataset and clean data from the text row
data = pd.read_table("CellLines_15Genes.txt",sep='\t',header=(0))
#Remove ID column to kep only numeric data
data=data.drop(['Id'], axis = 1)
#Convert integers to floats
datafinal = data.astype(float)
log = np.log(datafinal+1)
print(log.describe())
#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_table("CellLines_15Genes.txt",sep='\t',header=(0))
data=data.drop(['Id'], axis = 1)
#Convert integers to floats
datafinal = data.astype(float)
log = np.log(datafinal+1)
log.describe()
plt.figure(figsize=(20,16))
plt.boxplot(log)
plt.show()
plt.figure(figsize=(20,16))
plt.hist(log)
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Read the dataset and clean data from the text row. Make sure to use drag and drop option to upload file
data = pd.read_table("CellLines_15Genes.txt",sep='\t',header=(0))
#Create heatmap
plt.imshow(datafinal, cmap='viridis')
plt.colorbar()
plt.show()


#define our functions
def print_sequence_length():
  #store DNA strand as a string in the variable seq
  seq="AGTGTCCACTG"
  #returns the sequence length
  return len(seq)
#run our function
print(print_sequence_length())



# define reverse complement function
def reverse_complement_DNA(dna_sequence):
    # create reverse complemnt
    reverse_complement = dna_sequence.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[
                         ::-1]

    # return resulted output
    return reverse_complement

print(reverse_complement_DNA("ATGCCGTGGTAAAGCCTTAAG"))
