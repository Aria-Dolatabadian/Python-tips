Seq = "ACGUGTTTTTTACGAUUGUGACGA"
start = 5
stop = 10
if len(Seq) > stop :
    Seq2 = Seq[0: start:] + Seq[stop + 1::]
print(Seq2)
