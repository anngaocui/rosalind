lines=open("/home/ralf/Downloads/rosalind_lexf.txt","r").readlines()
d=lines[0].strip().split(" ")
print d
a=int(lines[1][0])
f=open("order.txt","w")
qq=[]
qq.append([])
qq[0].append([])
for j in range(a):
	qq.append([])
	for l in qq[j]:
		for n in d:
			qq[j+1].append(l+map(str,n))
for k in qq[a]:
	f.write("".join(map(str,k))+"\n")