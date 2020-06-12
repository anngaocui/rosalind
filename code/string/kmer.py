lines=open("/home/ralf/Downloads/rosalind_kmer.txt","r").readlines()[1:]
one=""
for line in lines:
	one=one+line.strip()
k=[a+b+c+d for a in "ACGT" for b in "ACGT" for c in "ACGT" for d in "ACGT"]
d={}
for i in range(len(one)-3):
	if one[i:i+4] not in d:
		d[one[i:i+4]]=1
	else:
		d[one[i:i+4]]=d[one[i:i+4]]+1
p=[]
for i in k:
	p.append(d[i])
print " ".join(map(str,p))
