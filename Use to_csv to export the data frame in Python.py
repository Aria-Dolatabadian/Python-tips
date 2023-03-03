df.to_csv("data.csv", sep=",")

penguins.to_csv("FileName.csv", index=False)

#from numpy
import numpy as np
from numpy import savetxt
savetxt('data.csv', data, delimiter=',')
