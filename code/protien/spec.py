pro=open("prot_weight.txt","r").readlines()
prot=[]
weight=[]
for i in pro:
	l=i.split("   ")
	prot.append(l[0])
	weight.append(l[1].strip())
weights=open("/home/ralf/Downloads/rosalind_spec.txt","r").readlines()
p=''
for j in range(1,len(weights)):
	k=float(weights[j].strip())-float(weights[j-1].strip())
	for i in range(len(weight)):
		if -0.02<float(weight[i])-k and float(weight[i])-k<0.02:			
			p=p+prot[i]
			break
print p