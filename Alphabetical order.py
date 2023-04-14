x = 'rice'
k = input('Name a crop: ')

if k < x:
     print('Your crop ' + k + ' is before ' + x)
elif k > x:
     print('Your crop ' + k + ' is after ' +x)
else:
     print('Your crop ' + k + ' is equal to ' + x)

     
     #or
     
     
     x = 'rice'

while True:
    k = input('Name a crop (or enter "quit" to exit): ')

    if k == 'quit':
        break
    elif k < x:
        print('Your crop ' + k + ' is before ' + x)
    elif k > x:
        print('Your crop ' + k + ' is after ' + x)
    else:
        print('Your crop ' + k + ' is equal to ' + x)
