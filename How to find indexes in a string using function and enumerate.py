def find():
 ls=[]
 x = "AAATAAAAAATAAA"
 for j,i in enumerate(x):
  if i == "T":
   ls.append(j)
 return ls
print(find())
