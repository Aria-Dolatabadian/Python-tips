name = input ("Your Name: ")
a= float(input ("Math: "))
b= float (input("Physics: "))
c= float(input("Python:  "))
d = float(input("Biology: "))
e= float(input("Biochemistry: "))
f= float(input("Chemistry: "))
g= float(input("Statistics: "))
Sum = ( a+b+c+d+e+f+g)
result = (Sum*100)
Average= (result/700)

print(Average)
if Average >90 :
 print("Congratulations " + name + " you passed")
elif Average <90:
 print("Sorry " + name + " you failed")
