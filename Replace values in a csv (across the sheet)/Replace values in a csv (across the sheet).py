import pandas as pd
dataframe = pd.read_csv("change.csv")
dataframe.replace(to_replace="RLK",
                  value="NBS",
                  inplace=True)
dataframe.replace(to_replace="RLP",
                  value="TX",
                  inplace=True)
dataframe.to_csv('d:\python\change2.csv',
                 index=False)
