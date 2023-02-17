x="UTCATCGUTCTAATGGCTTGTACUTC"
index = []
while True:
    if 'UTC' in x:
        index.append(x.find('UTC'))
        x = x.replace('UTC', "utc", 1)
    elif 'UTC' not in x:
        break
print(index)
