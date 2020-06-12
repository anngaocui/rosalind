lines=open("/home/ralf/Downloads/rosalind_gcon.txt","r").readlines()
ll=""
for line in lines:
	ll=ll+line.strip()
v,w=ll.split(">")[1][13:],ll.split(">")[2][13:]
blosum=open("blosum62.txt","r").readlines()#blosum62
blo={}
mm=blosum[0].strip().split("  ")
for i in range(1,len(blosum)):
	h=blosum[i].strip().split(" ") 
	for j in range(len(mm)):
		blo[h[0]+mm[j]]=(h[j+1])
def global_alignment_with_constant_gap(v, w, scoring_matrix, sigma):
	from numpy import zeros
	S_lower = zeros((len(v)+1, len(w)+1), dtype=int)
	S_middle = zeros((len(v)+1, len(w)+1), dtype=int)
	S_upper = zeros((len(v)+1, len(w)+1), dtype=int)
	for i in xrange(1, len(v)+1):
		S_lower[i][0] = -sigma
		S_middle[i][0] = -sigma
		S_upper[i][0] = -10*sigma
	for j in xrange(1, len(w)+1):
		S_upper[0][j] = -sigma
		S_middle[0][j] = -sigma
		S_lower[0][j] = -10*sigma
	for i in xrange(1, len(v)+1):
		for j in xrange(1, len(w)+1):
			S_lower[i][j] = max([S_lower[i-1][j], S_middle[i-1][j] - sigma])
			S_upper[i][j] = max([S_upper[i][j-1], S_middle[i][j-1] - sigma])
			S_middle[i][j] = max([S_lower[i][j], S_middle[i-1][j-1] + int(scoring_matrix[v[i-1]+w[j-1]]), S_upper[i][j]])
	max_score = S_middle[len(v)][len(w)]
	return max_score
if __name__ == '__main__':
	score = str(global_alignment_with_constant_gap(v,w,blo, 5))
	print score