lines=open("/home/ralf/Downloads/rosalind_scsp.txt","r").readlines()
ones=[]
i=-1
for line in lines:
	line=line.strip()		
	ones.append(line)
d=[[]]
for j in range(len(ones[0])+1):
	d[0].append(-j)
for i in range(len(ones[1])):
	d.append([-i-1])
	for j in range(len(ones[0])):
		if ones[1][i]==ones[0][j]:
			m=d[i][j]+1
			d[i+1].append(m)
		else:
			a=sorted([d[i+1][j],d[i][j+1]])[-1]
			d[i+1].append(a)
i=len(ones[1])
j=len(ones[0])
g=[]
longest_sseq=''
while i*j!=0:
	if d[i][j] == d[i-1][j]:
		longest_sseq = ones[1][i-1] + longest_sseq
		i -= 1
	elif d[i][j] == d[i][j-1]:
		longest_sseq = ones[0][j-1] + longest_sseq
		j -= 1
	else:
 		longest_sseq = ones[1][i-1] + longest_sseq
 		i -= 1
 		j -= 1
if j!=0:
	longest_sseq = ones[0][0:j] + longest_sseq
elif i!=0:
	longest_sseq = ones[0][0:i] + longest_sseq
print longest_sseq,len(longest_sseq)