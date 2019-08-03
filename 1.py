santhosh1 = int(input())
dn=[]
for i in range(0,santhosh1):
 lan2=input()
 dn.append(lan2)
thissss3=[]
for i in zip(*dn):
 if(i.count(i[0])==len2(i)):
  thissss3.append(i[0])
 
 else:
  break
print(''.join(thissss3))
