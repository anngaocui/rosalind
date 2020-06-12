pro=[line.strip()for line in open("/home/ralf/Downloads/rosalind_sgra.txt","r").readlines()]
w={"A":71.03711,"C":103.00919,"D":115.02694,"E":129.04259,"F":147.06841,"G":57.02146,"H":137.05891,"I":113.08406,"K":128.09496,"L":113.08406,"M":131.04049,"N":114.04293,"P":97.05276,"Q":128.05858,"R":156.10111,"S":87.03203,"T":101.04768,"V":99.06841,"W":186.07931,"Y":163.06333}
weight=[]
for a,b in zip(pro[0:-1],pro[1:]):
	weight.append(float(b)-float(a))
out=[]
m=0
def s(l):
	s=0
	for i in l:
		s=s+i
	return(s)
for i in range(len(weight)):
	for j in w:
		if m==i: 
			if abs(weight[i]-float(w[j]))<0.01:
				out.append(j)
				m=m+1
				break
		else:
			if abs(s(weight[m:i+1])-float(w[j]))<0.01:
				out.append(j)
				m=i+1
				ll=0
				break	
print "".join(out)


###
from rosalind import *
data = file(ROOT + 'SGRA.txt')
vertices = sorted(map(float,data.read().splitlines()))

G = nx.DiGraph()
for v,u in combinations(vertices, 2):
  dist, match = min((abs(x-(u-v)),x) for x in inv_weight_table)
  if dist<1e-3:
    G.add_edge(v,u,aa=inv_weight_table[match])

peptide = defaultdict(str)
for v in nx.topological_sort(G):
  if len(G.in_edges(v)) > 0:
    u = max(G.in_edges(v), key=lambda x: len(peptide[x[0]]))[0]
    peptide[v] = peptide[u]+G[u][v]['aa']

print max(peptide.values(), key=len)