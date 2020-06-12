lines=open("/home/ralf/Downloads/rosalind_eubt.txt","r").read().strip().split(" ")
line=[["("+lines[1]+","+lines[2]+")"],[]]
def eubt(lines):	
	n=0
	for add in lines[3:]:
		p={}
		q={}
		d={}
		k=[]
		for i in line[n]:
			m=1
			for j in range(len(i)):
				if i[j]=="(":
					p[m]=j
					k.append(m)
					m+=1
				elif i[j]==",":
					d[k[-1]]=j
				elif i[j]==")":
					q[k[-1]]=j
					k.pop()
			for f in p:
				line[n+1].append(i[:d[f]+1]+"("+ i[d[f]+1:q[f]]+","+add+")"+i[q[f]:])
				line[n+1].append(i[:p[f]]+"("+ i[p[f]:d[f]]+","+add+")"+i[d[f]:])
			line[n+1].append("("+i+","+add+")")
		n=n+1
		line.append([])
	return(line[n])
l=eubt(lines)
f=open("eubt.txt","w")
for i in l:
	print "("+i+")"+lines[0]+";"
	f.write("("+i+")"+lines[0]+";"+"\n")
f.close()