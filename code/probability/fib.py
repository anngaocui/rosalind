string=open("/home/ralf/Downloads/rosalind_gc.txt","r").readline()
n,k=string[0],string[1]
def	rabbit(n,k):
	pair=[1,1]
	if n<3:
		print 1
	else:
		for j in range(3,n+1,1):
			pair.append(pair[j-2]+pair[j-3]*k)
		print pair[n-1]
rabbit(n,k)