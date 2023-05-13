# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Build a dataframe with 4 connections
df = pd.DataFrame({'from': ['A', 'B', 'C', 'A', 'E', 'A', 'E'], 'to': ['D', 'A', 'E', 'C', 'B', 'E','D']})

# Build your graph
G = nx.from_pandas_edgelist(df, 'from', 'to')

# Pl
nx.draw(G, with_labels=True)
plt.show()
