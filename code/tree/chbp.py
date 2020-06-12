import re
lines=open("/home/ralf/Downloads/rosalind_chbp.txt","r").read().strip().split("\n")
species=lines[0].split(" ")
line=lines[1:]
def find(species,line):
	dic={}
	f=[]
	for i in line:
		l=re.finditer(r"1",i)
		k=re.finditer(r"0",i)
		d=[]
		p=[]
		for j in l:
			d.append(j.start())
		if len(d)==2:
			dic[i]=d
		for n in k:
			p.append(n.start())
		if len(p)==2:
			dic[i]=p
	for m in dic:
		species[dic[m][0]]="("+species[dic[m][0]]+","+species[dic[m][1]]+")"
		f.append(dic[m][1])
	for m in range(len(line)):
		for n in sorted(f)[::-1]:
			line[m]=line[m][:n]+line[m][n+1:]
	for n in sorted(f)[::-1]:
			species.pop(n)
	return(species,line)
while len(species)>3:
	species,line=find(species,line)
print "("+species[0]+","+species[1]+","+species[2]+")"