from numpy import zeros,unravel_index
sam250=open("sam250.txt","r").readlines()#SAM250矩阵
sam={}
mm=sam250[0].strip().split("  ")
for i in range(1,len(sam250)):
	h=sam250[i].replace("  "," ").strip().split(" ") 
	for j in range(len(mm)):
		sam[h[0]+mm[j]]=h[j+1]
lines=open("/home/ralf/Downloads/rosalind_loca.txt","r").readlines()#读文件
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
backtrack = zeros((len(v)+1, len(w)+1), dtype=int)
for i in xrange(1, len(v)+1):
	for j in xrange(1, len(w)+1): 
		scores =[S[i-1][j]-5, S[i][j-1]-5, S[i-1][j-1] + int(sam[v[i-1]+w[j-1]]),0]
		S[i][j] = max(scores)
		backtrack[i][j] = scores.index(S[i][j])
i,j = unravel_index(S.argmax(), S.shape)
max_score = str(S[i][j])
v_aligned, w_aligned = v[:i], w[:j]
while backtrack[i][j] != 3 and i*j != 0:
	if backtrack[i][j] == 0:
		i -= 1
	elif backtrack[i][j] == 1:
		j -= 1
	elif backtrack[i][j] == 2:
		i -= 1
		j -= 1
v_aligned = v_aligned[i:]
w_aligned = w_aligned[j:]
print "\n".join([max_score, v_aligned, w_aligned])