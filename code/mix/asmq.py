lines=open('/home/ralf/Downloads/rosalind_asmq.txt','r').readlines()
lenth=[]
sum=0.0
for line in lines:
	line=line.strip()
	lenth.append(len(line))
	sum=sum+len(line)
lenth=sorted(lenth)[::-1]
N50=sum*1/2
N75=sum*0.75
put=[]
qq=0
for i in lenth:
	qq=qq+i
	if qq>N50:
		put.append(i)
	if qq>N75:
		put.append(i)
		break
print put[0],put[-1]