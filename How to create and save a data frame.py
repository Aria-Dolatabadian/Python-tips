import pandas as pd
data = {'Month': ['Jan ','Feb ','Mar ','Apr ','May ','Jun '],
        'Aria': [1000,1500,1200,1400,1500,1800],
        'Alex': [2500,2200,2000,2100,2200,2600],
        }
df = pd.DataFrame(data,columns=['Month','Aria','Alex'])
print (df)
#  saving the dataframe
df.to_csv(r'd:\python\dataframe.csv', index=False)
