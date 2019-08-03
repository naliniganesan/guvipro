#mano
from itertools import combinations
sn,tn=input().split()
tn=int(tn)
top1=[]
van=len(sn)-tn
fake=combinations(sn,van)
for i in list(fake):
  top1.append("".join(i))
print(min(top1))
