def test(Name, Surname='Dolatabadian'):
    fullname=Name + ' ' + Surname
    return fullname
n=(input('Name:'))
m=(input('Surname:'))
print(test(n))
