#Triplet
un=int(input())
op=list(map(int,input().split()))
ct=0
for i in range(0,un-2):
	for j in range(1,un-1):
		for k in range(2,un):
			if(op[i]<op[j] and op[j]<op[k]):
				ct+=1
print(ct)
