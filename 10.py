paths=int(input())
bin1=[int(i) for i in input().split()]
pest5=0
for k in range(paths):
   for j in range(k):
      if bin1[j]<bin1[k]:
         pest5+=bin1[j]
print(pest5) 
