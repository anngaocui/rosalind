lines=open("/home/ralf/Downloads/rosalind_mgap.txt","r").readlines()
ll=""
for line in lines:
	ll=ll+line.strip()
v,w=ll.split(">")[1][13:],ll.split(">")[2][13:]
def maximum_gap_symbols(v, w):
	M = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
	for i in xrange(len(v)):
		for j in xrange(len(w)):
			if v[i] == w[j]:
				M[i+1][j+1] = M[i][j]+1
			else:
				M[i+1][j+1] = max(M[i+1][j],M[i][j+1])
	return len(v) + len(w) - 2*M[len(v)][len(w)]
print str(maximum_gap_symbols(v,w))