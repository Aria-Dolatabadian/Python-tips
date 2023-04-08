import pandas as pd

df1 = pd.read_csv('1.csv')
df2 = pd.read_csv('2.csv')

item_to_search = 'RLK'
count1 = df1[df1['RGA'] == item_to_search].shape[0]
count2 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count1}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count2}times in the second csv file.')
total_count = count1 + count2
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

item_to_search = 'RLP'
count3 = df1[df1['RGA'] == item_to_search].shape[0]
count4 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count3}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count4}times in the second csv file.')
total_count = count3 + count4
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

item_to_search = 'CN'
count5 = df1[df1['RGA'] == item_to_search].shape[0]
count6 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count5}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count6}times in the second csv file.')
total_count = count5 + count6
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

item_to_search = 'CNL'
count7 = df1[df1['RGA'] == item_to_search].shape[0]
count8 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count7}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count8}times in the second csv file.')
total_count = count7 + count8
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

item_to_search = 'TN'
count9 = df1[df1['RGA'] == item_to_search].shape[0]
count10 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count9}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count10}times in the second csv file.')
total_count = count9 + count10
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

item_to_search = 'TNL'
count11 = df1[df1['RGA'] == item_to_search].shape[0]
count12 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count11}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count12}times in the second csv file.')
total_count = count11 + count12
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

item_to_search = 'NBS'
count13 = df1[df1['RGA'] == item_to_search].shape[0]
count14 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count13}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count14}times in the second csv file.')
total_count = count13 + count14
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

item_to_search = 'TM-CC'
count15 = df1[df1['RGA'] == item_to_search].shape[0]
count16 = df2[df2['RGA'] == item_to_search].shape[0]
print(f'The item "{item_to_search}" appears {count15}times in the first csv file.')
print(f'The item "{item_to_search}" appears {count16}times in the second csv file.')
total_count = count15 + count16
print(f'The item "{item_to_search}" appears {total_count} times in the two CSV files.')

