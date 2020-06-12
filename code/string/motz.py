rna = "".join(open('/home/ralf/Downloads/rosalind_motz.txt',"r").read().strip().split("\n")[1:])
c = {'':1, 'A':1, 'C':1, 'G':1, 'U':1, 'AA':1, 'AC':1, 'AG':1, 'AU':2, 'CA':1, 'CC':1, 'CG':2, 'CU':1, 'GA':1, 'GC':2, 'GG':1, 
'GU':1, 'UA':2, 'UC':1, 'UG':1, 'UU':1}
def motzkin(s):
    if s not in c:
        c[s] = motzkin(s[1:]) + sum([motzkin(s[1:k]) * (c[s[0]+s[k]]-1) * motzkin(s[k+1:]) for k in range(1, len(s))])
    return c[s]
print motzkin(rna) % 10**6