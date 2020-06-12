n=int(open("/home/ralf/Downloads/rosalind_sset.txt","r").readline().strip())
sum_sub=2
x=1
s=1
for i in range(1,n):
	x=x*i
	s=s*(n-i+1)
	sum_sub=sum_sub+s/x
print sum_sub%1000000