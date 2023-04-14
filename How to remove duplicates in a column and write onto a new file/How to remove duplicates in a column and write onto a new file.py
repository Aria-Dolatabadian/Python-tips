inFile = open('Type.csv','r')
outFile = open('Type1.csv','w')
listLines = []
for line in inFile:
    if line in listLines:
        continue
    else:
        outFile.write(line)
        listLines.append(line)
outFile.close()
inFile.close()
