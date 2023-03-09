import pandas as pd
import numpy as np

a = pd.read_csv('x.csv')
print(type(a))

x = np.loadtxt('x.csv', delimiter=',')

print(type(x))
