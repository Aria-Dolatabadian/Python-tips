import random # Or secrets

def permTable(nc, sum, mn, mx):
  t=[[0 for i in range(sum+1)] \
    for j in range(nc+1)]
  t[0][0]=1
  for i in range(1,nc+1):
    for j in range(0,sum+1):
      jm=max(j-(mx-mn), 0)
      v=0
      for k in range(jm, j+1): v+=t[i-1][k]
      t[i][j]=v
  return t

def getSol(nc, sum, mn, mx, table):
  s=sum-nc*mn
  ret=[0 for i in range(nc)]
  for ib in range(nc):
    i=nc-1-ib
    # Or 'secrets.randint(table[i+1][s])'
    v=random.randint(0, table[i+1][s]-1)
    r=mn
    v-=table[i][s]
    while v>=0:
      v-=table[i][s-1]
      s-=1
      r+=1
    ret[i]=r
  return ret

def genAverage(numSamples, valuesPerSample, mn, mx, avg):
   sum = avg * valuesPerSample
   pt = permTable(valuesPerSample, sum, mn, mx)
   return [getSol(valuesPerSample, sum, mn, mx, pt) \
      for i in range(numSamples)]

# Print one sample
print(genAverage(1, 20, 1, 4, 1))
print(genAverage(1, 20, 1, 4, 2))
print(genAverage(1, 20, 1, 4, 3))
print(genAverage(1, 20, 1, 4, 4))
