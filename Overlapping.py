a=range(10,20)
b=range(15,22)
c=range(24,35)
z=range(25,33)
d=[]
e=[]
f=[]
g=[]
for x in a:
    d.append(x)
for x in b:
    e.append(x)
for x in c:
    f.append(x)
for x in z:
    g.append(x)
print(("D:"),(d))
print(("E:"),(e))
print(("F:"),(f))
print(("G:"),(g))
#
Overlapping = bool(set(d) & set(e))
print((Overlapping),("overlappong between d and e"))
Overlapping = bool(set(d) & set(f))
print((Overlapping),("overlappong between d and f"))
Overlapping = bool(set(d) & set(g))
print((Overlapping),("overlappong between d and g"))
Overlapping = bool(set(e) & set(f))
print((Overlapping),("overlappong between e and f"))
Overlapping = bool(set(e) & set(g))
print((Overlapping),("overlappong between e and g"))
Overlapping = bool(set(f) & set(g))
print((Overlapping),("overlappong between f and g"))
