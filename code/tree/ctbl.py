from numpy import zeros
from scripts import Newick
with open('/home/ralf/Downloads/rosalind_ctbl.txt') as input_data:
	newick_input = input_data.read().strip()
newick_tree = Newick(newick_input)
named_nodes = lambda n: 'Node_' not in n
unnamed_edges = lambda e: 'Node_' in e[0] and 'Node_' in e[1]
node_order = {name:index for index,name in enumerate(sorted(filter(named_nodes, [node.name for node in newick_tree.nodes])))}
nontrivial_edges = filter(unnamed_edges, newick_tree.edge_names())
M = zeros((len(nontrivial_edges), len(node_order)), dtype=int)
for i, edge in enumerate(nontrivial_edges):
	taxa = filter(named_nodes, set(newick_tree.get_descendants(edge[0])) & set(newick_tree.get_descendants(edge[1])))
	for t in taxa:
		M[i][node_order[t]] = 1
print '\n'.join([''.join(map(str, M[i])) for i in xrange(len(M))])
with open('output/056_CTBL.txt', 'w') as output_data:
	output_data.write('\n'.join([''.join(map(str, M[i])) for i in xrange(len(M))]))
##
with open('/home/ralf/Downloads/rosalind_ctbl_2_dataset.txt') as input_data:
	newick_input = input_data.read().strip()[:-1].replace(" ","")
m=-1
g=''
p=[]
dic={}
for i in newick_input:
	if i=="(":
		m=m+1
		p.append(m)
	elif i=="," or i==")":
		dic[g]=p[:]
		g=""
		if i==")":
			p=p[:-1]
	else:
		g=g+i
k=sorted(dic.keys())
for i in xrange(1,m+1):
	dic1={}
	ll=''
	for j in k:
		if i in dic[j]:
			dic1[j]="1"
		else:
			dic1[j]="0"
	for j in k:
		ll=ll+dic1[j]
	print ll