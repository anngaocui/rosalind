def trace(s,t,i,j,trax):
	ss=''
	tt=''
	while i>0:		
		if trax[i][j] ==trax[i-1][j-1]-1 :		
			tt = t[i-1]+tt
			ss = s[j-1]+ss
			i -= 1
			j -= 1	
		elif trax[i][j] ==trax[i-1][j]-1:
			tt= t[i-1]+tt
			ss = "-"+ss
			i -= 1
		elif trax[i][j] == trax[i][j-1]-1:
			tt = "-"+tt
			ss = s[j-1]+ss
			j-=1
		else:
			tt = t[i-1]+tt
			ss = s[j-1]+ss
			i -= 1
			j -= 1
	print ss
	print tt
from Bio import SeqIO
f = open("/home/ralf/Downloads/rosalind_sims.txt","r")
seqs = SeqIO.parse(f, "fasta")
seqs = [str(s.seq) for s in seqs]
s,t=seqs[0],seqs[1]
dd=[[]]
for i in range(len(s)+1):
	dd[0].append(0)
for j in range(len(t)+1):
	dd.append([])
	dd[j].append(0)
for i in range(1,len(t)+1):
	for j in range(1,len(s)+1):
		if t[i-1]==s[j-1]:
			dd[i].append(dd[i-1][j-1]+1)
		else:
			dd[i].append(max(dd[i-1][j-1]-1,dd[i-1][j]-1,dd[i][j-1]-1))
print max(dd[len(t)])
for i in range(len(s)):
	if dd[len(t)][i]==max(dd[len(t)]):
		break
trace(s,t,len(t),i,dd)