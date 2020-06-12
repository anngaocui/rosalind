n= int(open('/home/ralf/Downloads/rosalind_cntq.txt',"r").readline().strip())
print n*(n-1)*(n-2)*(n-3)/(4*3*2)%1000000