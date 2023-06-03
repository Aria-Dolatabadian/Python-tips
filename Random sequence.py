from random import choice
length=20
sequence=''
bases=['A','T','C','G']
#1
for i in range(length):
    base=choice(bases)
    sequence+=base
print(sequence)
#2
sequence=[choice(bases)for i in range (length)]
print(sequence)
#converts the list to a string
sequence=''.join(sequence)
print (sequence)
#3
sequence=''
while len(sequence)!=20:
    base=choice(bases)
    sequence+=base
print(sequence)
