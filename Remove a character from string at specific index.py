Seq = "ACTGUGACGAUUGUGACGA"
index = 2
if len(Seq) > index:
    Seq = Seq[0 : index : ] + Seq[index + 1 : :]
print(Seq)
