from Bio.Seq import Seq
lines=open("/home/ralf/Downloads/rosalind_corr.txt","r").readlines()
ff=open("ff.txt","w")
#ww=open("jj.txt","w")
m=[]
d=[]
f={}
for i in range(1,len(lines)+1,2):
	one=lines[i].strip()
	d.append(one)
	if one not in f:
		f[one]=1
		f[one[::-1].replace("A","t").replace("G","c").replace("C","g").replace("T","a").upper()]=1
	else:
		f[one]=f[one]+1
		f[one[::-1].replace("A","t").replace("G","c").replace("C","g").replace("T","a").upper()]+=1
for i in d:
	for j in d:
		q=sum(a!=b for a,b in zip(i,j))
		if q==1:
			if f[i]==1 and f[j]>=2:
				m.append(i+"->"+j)
			continue
		p=sum(a!=b for a,b in zip(i,j[::-1].replace("A","t").replace("G","c").replace("C","g").replace("T","a").upper()))
		if p==1:
			if f[i]==1 and f[j]>=2:
				m.append(i+"->"+j[::-1].replace("A","t").replace("G","c").replace("C","g").replace("T","a").upper())
			continue
for i in set(m):
	ff.write(i+"\n")
print len(f),len(d)