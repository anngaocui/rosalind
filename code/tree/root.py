n=int(open('/home/ralf/Downloads/rosalind_root.txt').readline().strip())
print reduce(lambda a, b: a*b % 10**6, xrange(2*n-5, 1, -2),(2*n-3))