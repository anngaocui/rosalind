#1
import sys
res = set()
def go (t, j, l):
  if l == n:
    if g[j][0]:
      res.add(t[:n])
      return
  for i in range(n):
    if u[i] == 0 and g[j][i]:
      u[i] = 1
      go(t + s[i][-1:], i, l+1)
      u[i] = 0
s = [t.strip() for t in open('/home/ralf/Downloads/rosalind_grep.txt').readlines()]
n = len(s)
g = [[(s[i][1:] == s[j][:-1]) for j in range(n)] for i in range(n)]
#print g
u = [0]*n
go (s[0], 0, 1)
print "\n".join(res)
'''
#2
def coverings(s, edges, k):
	add_on = [index for index, item in enumerate(edges) if item[0] == s[-k+1:]]
	if len(add_on) == 0:
		return [s if edges == [] else []]
	else:
		return [coverings(s+edges[i][1][-1], edges[:i]+edges[i+1:], k) for i in add_on]
def flatten(lst):
	for element in lst:
		if isinstance(element, list):
			for subelement in flatten(element):
				yield subelement
		else:
			yield element
if __name__ == '__main__':
	with open('/home/ralf/Downloads/rosalind_grep.txt') as input_data:
		k_mers = [line.strip() for line in input_data.readlines()]
	k = len(k_mers[0])
	edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
	DBG_edges = [edge(elmt) for elmt in k_mers[1:]]
	circular_strings = [circular[:len(k_mers)] for circular in set(flatten(coverings(k_mers[0], DBG_edges, k)))]
	print '\n'.join(circular_strings)
'''