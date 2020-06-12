import sys
import itertools
def sign_permutations(n):
    return [x for x in itertools.permutations(range(-n,0)+range(1, n+1), n) if set(range(1, n+1))==set(map(abs,x))]
n = int(open("/home/ralf/Downloads/rosalind_sign.txt","r").readline().strip())
perms = sign_permutations(n)
print len(perms)
print '\n'.join([' '.join(map(str,x)) for x in perms])