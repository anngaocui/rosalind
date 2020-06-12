def count_unrooted_binary_trees(n):
	return reduce(lambda a, b: a*b % 10**6, xrange(2*n-5, 1, -2))
#n=int(open('/home/ralf/Downloads/rosalind_cunr.txt').readline().strip())
n=5
count = count_unrooted_binary_trees(n)
print count