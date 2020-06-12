from numpy import zeros
lines=open("/home/ralf/Downloads/rosalind_ctea.txt","r").readlines()
ones=[]
i=-1
for line in lines:
	line=line.strip()
	if ">" in line:
		ones.append("")
		i+=1
	else:		
		ones[i]=ones[i]+line
def count_alignment(v, w):
	from numpy import zeros
	S = zeros((len(v)+1, len(w)+1), dtype=int)
	dynamic_count = zeros((len(v)+1, len(w)+1), dtype=int)
	modulus = 2**27 - 1 
	for i in xrange(0, len(v)+1):
		S[i][0] = i
		dynamic_count[i][0] = 1
	for j in xrange(1, len(w)+1):
		S[0][j] = j
		dynamic_count[0][j] = 1
	for i in xrange(1, len(v)+1):
		for j in xrange(1, len(w)+1):
			scores = [S[i-1][j-1] + (v[i-1] != w[j-1]), S[i-1][j]+1, S[i][j-1]+1]
			S[i][j] = min(scores)
			dynamic_count[i][j] += [0, dynamic_count[i-1][j-1]][scores[0] == S[i][j]]
			print [0, dynamic_count[i-1][j-1]]	
			dynamic_count[i][j] += [0, dynamic_count[i-1][j]][scores[1] == S[i][j]]
			dynamic_count[i][j] += [0, dynamic_count[i][j-1]][scores[2] == S[i][j]]
			dynamic_count[i][j] = dynamic_count[i][j] % modulus
		
	return dynamic_count[len(v)][len(w)]
if __name__ == '__main__':
	s,t=ones[0],ones[1]
	count = str(count_alignment(s, t))
	print count