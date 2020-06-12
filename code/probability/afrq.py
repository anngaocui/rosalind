from math import sqrt
with open('/home/ralf/Downloads/rosalind_afrq.txt') as input_data:
	A = map(float, input_data.read().strip().split())
	B = [2*sqrt(i)-i for i in A]#a_=2Aa+aa  a:sqrt(aa) A:1-sqrt(aa)
print ' '.join(map(str,B))
with open('AFRQ.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,B)))