import pandas as pd
import numpy as np

a = pd.read_csv('x.csv')
print(type(a))

x = np.loadtxt('x.csv', delimiter=',')

print(type(x))




#You can convert a CSV file with first-line header to a NumPy array by calling np.loadtxt() with three arguments: 
#the filename, skiprows=1 to skip the first line (header), and the delimiter string. 
#For example, the expression
#np.loadtxt('my_file.csv', skiprows=1, delimiter=',') 
#returns a NumPy array from the 'my_file.csv' with delimiter symbols ',' while skipping the first line.
