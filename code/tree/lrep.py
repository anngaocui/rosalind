raw_data =open('/home/ralf/Downloads/rosalind_lrep.txt').readlines()
pat= raw_data[0].strip()#string
k = int(raw_data[1].strip())#positive integer
node_info = [line.strip().split() for line in raw_data[2:]]#edges
tree = {}
for n in node_info:
    if n[0] not in tree:
        tree[n[0]]=[None,'',0]
    if n[1] not in tree:
        tree[n[1]]=[n[0],tree[n[0]][1]+pat[int(n[2]):int(n[2])+int(n[3])],0]
leaves = filter(lambda x: '$' in tree[x][1], tree.keys())
for x in leaves:
    d = tree[x][0]
    while d is not None:
        tree[d][2] += 1
        d = tree[d][0]
cand = filter(lambda x: tree[x][2]>=k, tree.keys())
print tree[max(cand,key=lambda x:len(tree[x][1]))][1]