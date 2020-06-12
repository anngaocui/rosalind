lines=open("/home/ralf/Downloads/rosalind_pmch.txt","r").readlines()
ones=[]
i=-1
for line in lines:
	line=line.strip()
	if ">" in line:
		ones.append("")
		i+=1
	else:		
		ones[i]=ones[i]+line
d=[]
k=-1
print ones[1]
for i in ones[1]:
	for j in range(k+1,len(ones[0])):
		if i==ones[0][j] :
			d.append(j+1)
			k=j
			break
print " ".join(map(str,d))