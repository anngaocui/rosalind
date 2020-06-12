f=map(float,open("/home/ralf/Downloads/rosalind_sexl.txt","r").readline().strip().split(" "))
d=[]
for i in f :
	d.append(str(i*(1-i)*2))
print " ".join(d)