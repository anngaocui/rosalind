from math import factorial as fact
#n:diploid  m: copies  g: generations at least k copies 
N,m,g,k=map(int,open('/home/ralf/Downloads/rosalind_wfmd.txt',"r").read().strip().split(" "))
p_rec = 1.0 - (m/(2.0*N))
p = [fact(2*N)/(fact(i)*fact(2*N-i))*((p_rec)**i)*(1.0-p_rec)**(2*N-i) for i in range(1,2*N+1)]#probability
for gen in range(2,g+1):
	temp_p = []
	for j in range(1,2*N+1):
		temp_term = [fact(2*N)/(fact(j)*fact(2*N-j))*((x/(2.0*N))**j)*(1.0-(x/(2.0*N)))**(2*N-j) for x in range(1,2*N+1)]
		temp_p.append(sum([temp_term[i]*p[i] for i in range(len(temp_term))]))
	print temp_term
	p = temp_p
prob = sum(p[k-1:])
print prob