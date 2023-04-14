with open('1.csv', 'r') as t1, open('2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('Difference.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
            
#or



with open('1.csv', 'r') as t1, open('2.csv', 'r') as t2:
    filecoming = t1.readlines()
    filevalidation = t2.readlines()

for i in range(0,len(filevalidation)):
    coming_set = set(filecoming[i].replace("\n","").split(","))
    validation_set = set(filevalidation[i].replace("\n","").split(","))
    ReceivedDataList=list(validation_set.intersection(coming_set))
    NotReceivedDataList=list(coming_set.union(validation_set)-
    coming_set.intersection(validation_set))
    print(NotReceivedDataList)
