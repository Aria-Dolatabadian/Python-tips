import random
fid = open("entry.csv", "r")
li = fid.readlines()
fid.close()
print(li)
random.shuffle(li)
print(li)
fid = open("shuffled.csv", "w")
fid.writelines(li)
fid.close()
#see wd
