data = [
    ['Hyola', 'Susceptible'],
    ['Yetna', 'Resistant'],
    ['ATR Bonito', 'Susceptible'],
    ['ATR Wahoo', 'Resistant'],
]
len_marvel_data = len(data)
print()
print("|{0:->7}{0:->21}{1:-<25}|".format("|", ""))
print("{:^3}| {:^18} | {}".format("|index ","Cultivar","Susceptible/Resistant   |"))
print("|{0:->7}{0:->21}{1:-<25}|".format("|", ""))
for i in range(len_marvel_data):
    print(f"|{i:<4}  | {data[i][0]:<18} | {data[i][1]:<23} |")
print("|{0:->7}{0:->21}{1:-<25}|".format("|", ""))
