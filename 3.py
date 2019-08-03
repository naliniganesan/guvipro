pcc,vil=input().split()
AS1=abs(len(pcc)-len(vil))
for i in range(len(pcc)):
  if len(vil)==1 and vil[i] in pc:
   break
  if pcc[i]!=vil[i]:
   AS1+=1
print(AS1)
