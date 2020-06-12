lines=open("/home/ralf/Downloads/rosalind_cons.txt","r").readlines()
L=[[],[],[],[],[],[],[]]#存放频数，字符，列表
i=-1
for one in lines:
	one=one.strip()
	if ">" not in one:
		L[5][i]=L[5][i]+str(one)
	else:
		i=i+1
		L[5].append("")
for i in range(len(L[5][0])):
	l=[]
	for j in range(len(L[5])):
		l.append(L[5][j][i])
	large=""
	MAX=0
	for k,m in zip(["A","C","G","T"],range(4)):
		L[m].append(str(l.count(k)))
		if MAX<l.count(k):
			large=k
			MAX=l.count(k)
	L[4].append(large)
print "".join(L[4])
for a,i in zip(["A","C","G","T"],range(4)):
	print a+":"," ".join(L[i])