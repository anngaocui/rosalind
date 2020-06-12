from numpy import zeros
lines=open("/home/ralf/Downloads/rosalind_gaff.txt","r").readlines()
ones=[]
i=-1
for line in lines:
	line=line.strip()
	if ">" in line:
		ones.append("")
		i+=1
	else:		
		ones[i]=ones[i]+line
s,t=ones[0],ones[1]
M = zeros((len(s)+1,len(t)+1), dtype=int)
for i in range(1,len(s)+1):
	M[i][0]= i
for i in range(1,len(t)+1):
	M[0][i]= i
for i in xrange(1,len(s)+1):
	for j in xrange(1,len(t)+1):
		if s[i-1] == t[j-1]:
			M[i][j] = M[i-1][j-1]
		else:
			M[i][j] = min(M[i-1][j]+1,M[i][j-1]+1)
blosum=open("blosum62.txt","r").readlines()#blosum62
blo={}
mm=blosum[0].strip().split("  ")
for i in range(1,len(blosum)):
	h=blosum[i].strip().split(" ") 
	for j in range(len(mm)):
		blo[h[0]+mm[j]]=float(h[j+1])
j=len(ones[1])
i=len(ones[0])
l1=''
l2=''
m=0
d1=d2=0
pp=0
while i*j!=0:
	if M[i][j]-1 == M[i-1][j]:
		d1=1
		l1= ones[0][i-1] + l1
		l2="-"+l2
		i -= 1
	elif M[i][j]-1 == M[i][j-1]:
		d2=1
		l2 = ones[1][j-1] + l2
		l1="-"+l1
		j -= 1
	else:
		pp=pp+d1+d2
		d1=d2=0
		m=m+int(blo[ones[0][i-1]+ones[1][j-1]])
		print blo[ones[0][i-1]+ones[1][j-1]],ones[0][i-1],ones[1][j-1]
		l1= ones[0][i-1] + l1
		l2= ones[1][j-1] + l2
 		i -= 1
 		j -= 1
if j!=0:
	l1= ones[1][0:j-1] + l1
	l2="-"*j+l2
elif i!=0:
	l2= ones[0][0:i-1] + l2
	l1="-"*i+l1
print m-(pp*10+len(l1)*2-len(ones[1])-len(ones[0]))
print l1
print l2
print pp,len(l1)*2-len(ones[1])-len(ones[0])