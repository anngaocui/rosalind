one=open("/home/ralf/Downloads/rosalind_aspc.txt","r").readline().strip().split(" ")
sum_sub=1
x=1
s=1
for i in range(int(one[1]),int(one[0]))[::-1]:
	x=x*(int(one[0])-i)
	s=s*(i+1)
	sum_sub=sum_sub+s/x
print sum_sub%1000000