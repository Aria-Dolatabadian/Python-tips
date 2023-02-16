def test1(x,y):
    return (x-y)
def test2(x,y):
    return (x*y)
def test3(x,y):
    return(x+y)
def test4(x,y):
    return(x/y)
c=int(input('First number:'))
d=int(input('Second number:'))
e=int(input('1=Subtraction 2=Multiplication 3=Addition 4=Division'))
if e==1:
    print('Subtraction')
    print(test1(c,d))
elif e==2:
    print('Multiplication')
    print(test2(c,d))
elif e==3:
    print('Addition')
    print(test3(c, d))
elif e==4:
    print('Division')
    print(test4(c,d))
else:
    print('Error')
