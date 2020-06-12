trees=open('/home/ralf/Downloads/rosalind_nkew_3_dataset.txt').read().split("\n\n")
for i in trees:
	dd={}#name_weight
	pp={}#name_index
	kk=[]#name
	k_weight=[]#tree_weight
	for j in i.split("\n")[0][:-1].replace("(","").replace(")","").split(","):
		kk.append(j.split(":")[0])
		dd[j.split(":")[0]]=j.split(":")[1]#name_weight 1
	find=i.split("\n")[1].split(" ")#find name
	for j in i.split("\n")[0].split("):")[1:]:
		j=j.split(",")[0]
		k_weight.append(int(j.split(")")[0]))#tree_weight 2
	m=0
	n=1
	p=[]#record
	g=''
	q=[]#index
	k=[]#tree_index
	jj={1:0}
	for i in i.split("\n")[0][:-1]:
		if i=="("or i==")" or i==",":
			if g!="":
				if n==1:
					q.append(p[:])
					g=''
				else:
					n=1
			if i=="(":
				m=m+1 
				p.append(m)
			elif i==")":
				k.append(int(p[-1]))
				p=p[:-1]
				n=0
			g=''
		else:
			g=g+i  
	for i in range(len(k_weight)):
		jj[k[i]]=k_weight[i]
	for i in range(len(kk)):
		pp[kk[i]]=q[i]
	mm=[]
	for i in pp[find[0]]:
		if i not in pp[find[1]]:
			mm.append(i)
	for i in pp[find[1]]:
		if i not in pp[find[0]]:
			mm.append(i)
	ww=0
	for i in mm:
		ww=ww+int(jj[i])
	ww=ww+int(dd[find[0]])+int(dd[find[1]])
	print ww