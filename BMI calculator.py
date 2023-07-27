height = float(input("Your height in metres:"))
weight = int(input("Your weight in kilograms:"))
bmi = round(weight/ (height * height),2)
if bmi <= 18.5:
     print('Your BMI is', bmi, 'which means you are underweight.')
elif bmi > 18.5 and bmi < 25:
     print('Your BMI is', bmi, 'which means you are normal.')
elif bmi > 25 and bmi < 30:
     print('Your BMI is', bmi, 'which means you are overweight.')
elif bmi > 30 and bmi <35:
     print('Your BMI is', bmi, 'which means you are obese.')
elif bmi > 35 :
    print('Your BMI is', bmi, 'which means you are extremely obese.')
else:
    print('There is an error with your input')

#or

def test(x,y):
    return round(x/(y*y),2)
c=int(input("Weight (kg):"))
d=float(input('Height (m):'))
print('BMI:',test(c, d))
if test(c,d) <= 18.5:
    print('You are under weight')
elif test(c,d) > 18.5 and test(c,d) < 25:
     print('You are normal')
elif test(c,d) > 25 and test(c,d) < 30:
     print('You are overweight')
elif test(c,d) > 30 and test(c,d) <35:
     print('You are obese')
elif test(c,d) > 35 :
    print('You are extremely obese')
else:
    print('There is an error with your input')
