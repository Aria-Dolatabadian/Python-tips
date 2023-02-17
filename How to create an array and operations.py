from array import *
array1= array('i',[10,20,30,40,50])
for x in array1:
    print(x)
print('...................')
print ("first element:")
print (array1[0])
print ("third element:")
print (array1[2])
print('.....................')
array1.insert(1,60)
for x in array1:
    print(x)
print('.....................')

array1.remove(40)
for x in array1:
    print(x)
print('.....................')

print(array1.index(50))
print('.....................')
array1[3]=100
for x in array1:
    print(x)
