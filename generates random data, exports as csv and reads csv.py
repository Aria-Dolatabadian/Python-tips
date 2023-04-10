import pandas as pd
import numpy as np
data = np.random.rand(50, 4)
np.savetxt('data.csv', data, delimiter=',')
data = pd.read_csv('data.csv', header=None).values
print(data)
print(type(data))
