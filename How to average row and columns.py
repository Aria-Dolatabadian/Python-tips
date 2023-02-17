import pandas as pd

data = {'Month': ['Jan ','Feb ','Mar ','Apr ','May ','Jun '],
        'Jon Commission': [7000,5500,6000,4500,8000,6000],
        'Maria Commission': [10000,7500,6500,6000,9000,8500],
        'Olivia Commission': [3000,6000,4500,4500,4000,5500]
        }

df = pd.DataFrame(data,columns=['Month','Jon Commission','Maria Commission','Olivia Commission'])
print(df)


av_column = df.mean(axis=0)
print (av_column)

av_row = df.mean(axis=1)
print (av_row)
