lines=open("/home/ralf/Downloads/rosalind_splc.txt","r").readlines()
one=[]
i=-1
for line in lines:
	line=line.strip()
	if ">" in line:
		one.append("")
		i+=1
	else:		
		one[i]=one[i]+line
for k in one:
	for i in range(1,len(one)):
		one[0]="".join(one[0].split(one[i]))		
cod=open("RNAcodon.txt","r").readlines()
codon={}
codon[l.split(" ")[0]]=l.split(" ")[1].strip() for l in t.split("   ") for t in line.split("      ") for line in cod
pro=[]
print one[0]
one[0]=one[0].replace("T","U")
print len(one[0])
for i in range(0,len(one[0]),3):
	if i+3>len(one[0]):
		break
	else:
		if codon[one[0][i:i+3]]!="Stop":
			pro.append(codon[one[0][i:(i+3)]])
print "".join(pro)