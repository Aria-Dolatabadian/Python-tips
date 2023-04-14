with open('1.csv', 'r') as t1, open('2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('Difference.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
