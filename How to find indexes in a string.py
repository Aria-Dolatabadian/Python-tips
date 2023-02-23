x = "AAATAAAAAATAAA"
ls = []
for i in x:
    if i=="T":
        ls.append(x.find("T"))
        x = x.replace('T', 't', 1)
print(ls)
