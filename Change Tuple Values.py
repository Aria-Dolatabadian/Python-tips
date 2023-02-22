Rlm = ("Rlm1", "Rlm3", "Rlm3")
print(Rlm)
print(type(Rlm))

newRlm = list(Rlm)
print(newRlm)
print(type(newRlm))

newRlm[1] = "Rlm2"
print(newRlm)

Rlm = tuple(newRlm)
print(Rlm)
print(type(Rlm))
