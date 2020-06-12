import sys
import itertools
def main():
    alphabet, n = read_file('/home/ralf/Downloads/rosalind_lexv.txt')
    n = int(n)

    alphabet = ['_'] + alphabet.split(' ')
    permutations = ["".join(p).rstrip('_') for p in itertools.product(alphabet, repeat=n)]
    print "\n".join([p for p in permutations[1:] if '_' not in p])

def read_file(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

if __name__ == '__main__':
    main()