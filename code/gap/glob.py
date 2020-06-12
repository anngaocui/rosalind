def global_alignment_score(v, w,sigma):

	blosum=open("blosum62.txt","r").readlines()#blosum62
	blo={}
	mm=blosum[0].strip().split("  ")
	for i in range(1,len(blosum)):
		h=blosum[i].strip().split(" ") 
		for j in range(len(mm)):
			blo[h[0]+mm[j]]=(h[j+1])

	S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]	
	for i in xrange(1, len(v)+1):
		S[i][0] = -i*5
	for j in xrange(1, len(w)+1):
		S[0][j] = -j*5
	for i in xrange(1, len(v)+1):
		for j in xrange(1, len(w)+1):
			scores = [S[i-1][j] - 5, S[i][j-1] - 5, S[i-1][j-1] + int(blo[v[i-1]+w[j-1]])]
			S[i][j] = max(scores)
	return S[len(v)][len(w)]

if __name__ == '__main__':
	lines=open("/home/ralf/Downloads/rosalind_glob.txt","r").readlines()
	ones=[]
	i=-1
	for line in lines:
		line=line.strip()
		if ">" in line:
			ones.append("")
			i+=1
		else:		
			ones[i]=ones[i]+line
	s,t=ones[0],ones[1]#two string
	score = str(global_alignment_score(s, t, 5))
print score