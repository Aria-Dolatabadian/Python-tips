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
#or

text = open("change.csv", "r")
text = ''.join([i for i in text])
text = text.replace("RLK", "NBS")
x = open("d:\python\change2.csv", "w")
x.writelines(text)
x.close()
