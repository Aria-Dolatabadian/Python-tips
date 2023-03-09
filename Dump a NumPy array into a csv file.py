import numpy as np
import pandas as pd
x = np.random.random(size=2000) * 1000
np.savetxt("df.csv", x, delimiter=",")
