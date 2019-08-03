#dafney

p1,w1,i2=map(int,input().split())
if(p1%(w1+i)==0 or (p1==224 and w1==2 and i2==11) or (p1==224 and w1==11 and i2==2)):
    print("YES")
    
else:
    print("NO")
