ff=open('/home/ralf/Downloads/rosalind_qrt.txt',"r").read().strip().split("\n")
name=ff[0].split(" ")
table=ff[1:]
def ss(l):#
	aa=[]
	for i in range(len(l)-1):
		for j in range(i+1,len(l)):
			aa.append("{"+l[i]+","+l[j]+"}")
	return(aa)
dd=[]
for i in range(len(table)):
	A=[]
	B=[]
	for j in range(len(name)):		
		if str(table[i][j])=="1":
			A.append(name[j])
		elif str(table[i][j])=="0":
			B.append(name[j])
		else:
			pass
	if len(A)<2 or len(B)<2:
		continue
	else:
		for m in ss(A):
			for n in ss(B):
				if n+" "+m not in dd and m+" "+n not in dd:
					dd.append(m+" "+n)
gg=open("sqrtest.txt","w")
for i in dd:
	gg.write(i+"\n")