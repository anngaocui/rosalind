from scipy.stats.distributions import binom
from numpy import log10

if __name__ == "__main__":
    # n = int(open('/home/ralf/Downloads/rosalind_indc.txt').read().strip())
    n = 5
    B = binom(2 * n, 0.5)
    prob = [log10(B.sf(k)) for k in range(2 * n)]
    # print(" ".join(str("%.3f" % x) for x in prob))


def indc():
    from math import log10
    from math import factorial as fact
    # n = int(open('/home/ralf/Downloads/rosalind_indc.txt').read().strip()) * 2
    n = 10
    pp = ''
    for i in range(1, n + 1):
        p = 0
        for j in range(i, n + 1):
            p += ((fact(n)) / (fact(n - j)) / (fact(j))) * (0.5 ** n)
        pp = pp + " " + str("%.3f" % log10(p))
    print pp
