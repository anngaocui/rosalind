string=open("/home/ralf/Downloads/rosalind_lia.txt","r").readline()
n,k=string.split(" ")
n=int(n)
k=int(k)
t=2**n
print t,n,k
sum1=0
for a in range(k):
	T=1
	for i in range(a+1,t+1):
		T=T*i
	c=1
	for i in range(1,t-a+1):
		c=c*i
	sum1=sum1+(0.75**(t-a))*(0.25**a)*T/c
print 1-sum1
