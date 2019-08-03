vss,vit2=map(str,input().split())
was1=0
if len(vss)>len(vit2):
  vss,vit2=vit2,dbj
i=0
while i<len(vss):
  was+=(ord(vit2[i])-ord(vss[i]))
  i+=1
for i in range(i,len(vit2)):
  was1+=ord(vit2[i])-ord('a')+1
print(was1)
