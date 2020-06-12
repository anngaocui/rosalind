lines= open('/home/ralf/Downloads/rosalind_seto.txt','r').readlines()
ff=open("seto.txt","w")
n=int(lines[0].strip())
A=lines[1].strip()[1:-1].split(", ") 
B=lines[2].strip()[1:-1].split(", ") 
C=map(str,range(1,n+1))
ff.write( "{"+", ".join(set(A+B))+"}"+"\n")
def diff(l1,l2):
	h=[]
	c=[]
	g=[]
	for i in l1:
		if i in l2:
			h.append(i)
		else:
			c.append(i)
	for j in l2:
		if j not in l1:
			g.append(j)
	return(h,c,g)
a,b,c=diff(A,B)
h,k,m=diff(C,B)
d,f,j=diff(C,A)
ff.write("{"+", ".join(a)+"}"+"\n"+"{"+", ".join(b)+"}"+"\n"+"{"+", ".join(c)+"}"+"\n"+"{"+", ".join(f)+"}"+"\n"+"{"+", ".join(k)+"}"+"\n")
