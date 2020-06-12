lines=open("/home/ralf/Downloads/rosalind_pdst.txt","r").readlines()
d=[]
j=-1
for i in range(len(lines)):
	l=lines[i].strip()
	if ">" in l :
		d.append('')
		j+=1
	else:
		d[j]=d[j]+l
matrix=[]
i=0
for l1 in d:
	matrix.append([])
	for l2 in d:
		f=sum(a!=b for a,b in zip(l1,l2))
		matrix[i].append(f*1.0/len(l1))
	i+=1
for  i in matrix:
	print " ".join('%.7s'% v for v in i)