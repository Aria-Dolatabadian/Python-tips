#Sort the list alphabetically
x = ["A", "C", "B", "Y", "Z", '3', "5"]
x.sort()
print(x)
print('...........')
#Sort Descending
x.sort(reverse = True)
print(x)
print('.............')
#Sort the list numerically
list = [100, 50, 45, 12, 20]
list.sort()
print(list)
print('...........')
#Sort Descending
list.sort(reverse = True)
print(list)
print("...........")
#Customize Sort Function
#Sort the list based on how close the number is to 50
def f(n):
  return abs(n - 50)
list = [100, 50, 25, 10, 2]
list.sort(key = f)
print(list)
