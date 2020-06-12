a=int(open("/home/ralf/Downloads/rosalind_perm.txt","r").readline().strip())
import itertools 
q=list(itertools.permutations(range(1,a+1)))
q=map(list,q)
def enu(q):
	op={}
	qq=[]
	for i in range(a):
		qq.append(q)
		for l in qq[i]:
			qq.append([])
			for n in range(len(l)):
				op[" ".join(map(str,l[0:n]+[(-1*int(l[n]))]+l[n+1:]))]=1
				qq[i+1].append(map(str,l[0:n]+[(-1*int(l[n]))]+l[n+1:]))
	print len(op)
	for i in op.keys():
		print i
enu(q)