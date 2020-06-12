string=open("/home/ralf/Downloads/rosalind_prot.txt","r").readline()
#氨基酸表格处理成字典
try:
	rcodon=open("rnacodon.txt","r")
except:
	print "fileError"
cod=rcodon.readlines()
codon={}
for line in cod:
	one=line.split("      ")
	for t in one:
		ll=t.split("   ")
		for l in ll:
			k=l.split(" ")
			codon[k[0]]=(k[1].strip())

pro=[]
for i in range(0,len(string),3):
	if codon[string[i:(i+3)]]=="Stop":
		break
	else:
		pro.append(codon[string[i:(i+3)]])
print "".join(pro)