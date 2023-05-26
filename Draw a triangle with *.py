n= int(input("Input number:"))
for i in range(n):
    print(i)
for i in range(1, n+1):
    print(i)
for i in range(1, n+1):
    print("*"*i)
for i in range(1, n+1, 2):
    print("*"*i)
for i in range(1, n+1, 2):
    print(("*"*i).center(n))
