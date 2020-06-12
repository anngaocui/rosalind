import math    
if __name__ == "__main__":
    s= open('/home/ralf/Downloads/rosalind_prob.txt','r').readlines()
    string= s[0].strip()
    array = [float(x) for x in s[1].split()]
    gc = s.count('C')+s.count('G')
    at = len(string) - gc
    barray = []
    for x in range(len(array)):
        barray.append(math.log10((array[x]/2)**gc*(0.5-array[x]/2)**at))
    print ",".join(map(str,barray))
   # for x in range(len(array)):
    #    print barray[x]