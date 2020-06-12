f=open("trie.txt","w")
with open('/home/ralf/Downloads/rosalind_trie.txt') as input_data:
	dna = [line.strip() for line in input_data.readlines()]
one=[[]]
two=[[]]
mkm=[0]
for j in range(len(dna[0])):
	one[0].append(j+1)
	two[0].append(j+2)
	f.write(str(one[0][j])+" "+str(two[0][j])+" "+dna[0][j]+"\n")
for i in range(1,len(dna)):
	one.append([])
	two.append([])
	m=0
	l=0
	for j in range(i):
		k=0
		for n in range(len(dna[j])):
			if dna[i][n]==dna[j][n]:
				k=k+1
				if k>m:
					m=k
					l=j
			else:
				break
	mkm.append(m)
	if m==0:
		one[i].append(1)
	else:
		one[i].append(one[l][m]-mkm[l])
	two[i].append(two[i-1][-1]+1)
	f.write(str(one[i][0])+" "+str(two[i][0])+" "+dna[i][m]+"\n")
	for g in range(m+1,len(dna[i])):
		one[i].append(two[i][g-1-m])
		two[i].append(two[i][g-1-m]+1)
		f.write(str(one[i][g-m])+" "+str(two[i][g-m])+" "+dna[i][g]+"\n")