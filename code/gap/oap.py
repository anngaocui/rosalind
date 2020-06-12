from numpy import zeros,unravel_index
lines=open("/home/ralf/Downloads/rosalind_oap.txt","r").readlines()
ones=[]
i=-1
for line in lines:
	line=line.strip()
	if ">" in line:
		ones.append("")
		i+=1
	else:		
		ones[i]=ones[i]+line
v,w=ones[0],ones[1]
S = zeros((len(v)+1, len(w)+1), dtype=int)
for i in xrange(1, len(v)+1):
	for j in xrange(1, len(w)+1): 
		S[i][j] = max([S[i-1][j]-2, S[i][j-1]-2,S[i-1][j-1] -[2,-1][v[i-1]==w[j-1]]])

m=kk=0
for j in xrange(1, len(w)+1): 
		S[len(v)][j] = max([S[len(v)-1][j]-2, S[len(v)][j-1]-2,S[len(v)-1][j-1] -[2,-1][v[len(v)-1]==w[j-1]]])
		if S[len(v)][j]>m:
			m=S[len(v)][j]
			kk=j
print m,kk
'''
m=max(S[len(v)])
print m
q=S[len(v)]
kk=0
for j in range(len(w)):
	if m!=q[j]:
		kk=kk+1
	else:
		break
print m,kk
'''
l1=v[len(v)-kk:]
n=len(v)
l2=w[:kk]
i=kk
j=kk
if i*j!=0:
	if S[n][kk]==S[n-1][kk]+2:
		l2.insert(j,"-")
		j-=1
		n-=1
	elif S[n][kk]==S[n][kk-1]+2:
		l1.insert(i,"-")
		i-=1
		kk-=1
print l1,len(l1)
print l2,len(l2)