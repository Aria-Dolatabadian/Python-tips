data = data2 = ""

with open('A.txt') as fp:
    data = fp.read()

with open('B.txt') as fp:
    data2 = fp.read()

with open('C.txt') as fp:
    data3 = fp.read()

with open('D.txt') as fp:
    data4 = fp.read()

data += "\n"
data += data2

data += "\n"
data += data3

data += "\n"
data += data4

with open('Merged.txt', 'w') as fp:
    fp.write(data)
