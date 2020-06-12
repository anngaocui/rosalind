line=open("/home/ralf/Downloads/rosalind_pper.txt","r").readline()
line=line.split(" ")
n,k=int(line[0]),int(line[1].strip())
m=1
for i in range(n-k+1,n+1):
	m=m*i
print m%1000000