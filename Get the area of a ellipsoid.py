r1 = float(input(' Please Enter the a axis of a Ellipsoid: '))
r2 = float(input(' Please Enter the b axis of a Ellipsoid: '))
r3 = float(input(' Please Enter the c axis of a Ellipsoid: '))
pi = 3.1415926535897931
V= (((((r1*r2)**1.6  +  (r1*r3)**1.6  +  (r2*r3)**1.6)/3))**0.625)*4*pi
print('The surface area of the Ellipsoid is ~',V)
