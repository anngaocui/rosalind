lines=open("/home/ralf/Downloads/rosalind_lcsm.txt","r").readlines()
line=[]
i=-1
for one in lines:
	one=one.strip()
	print len(one)
	if ">" not in one:
		line[i]=line[i]+str(one)
	else:
		i=i+1
		line.append("")
dex={}
a=len(line)
j=20
for i in range(len(line[1])):
	if i+j>len(line[1]):
		break
	else:
		mo=line[0][i:i+j]
		n=1
		while n>0:
			mo=line[0][i:i+j]
			H=0
			for m in range(1,a):
				if mo in line[m]:
					H=H+1
				else:
					n=0
					break
			if H ==a-1:
				print line[0][i:i+j]				
				j=j+1