import math
ns11,ms11=map(int,input().split())
sn=[]
ar=list(map(int,input().split()))
for i in range(0,ms11):
    l1,h1=map(int,input().split())
    sp.append([l1,h1])
for i in sn:
    ss=i[0]-1
    oo=i[1]-1
    print(math.gcd(ar[ss],ar[oo]))
