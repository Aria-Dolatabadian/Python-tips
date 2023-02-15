
temp = 4
if temp<10:
    print('less')
    if temp%2==0:
        print('even')
        if temp%4==0:
            print("divisible by four")
        else:
            print('no')
    else:
        print("odd")
else:
    print("more")
