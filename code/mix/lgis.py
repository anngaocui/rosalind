lines=open("/home/ralf/Downloads/rosalind_lgis.txt","r").readlines()
m=int(lines[0].strip())##a number
ss=map(int,lines[1].strip().split(" ")) # list
def get_lis( ss ):   #Longest increasing subsequence
    import numpy as np
    lis = [ 1 ]*len(ss)
    for i in xrange( 1, len(ss)):
        for j in xrange( 0, i ):
            if ss[ i ] > ss[ j ]:
                lis[ i ] = max( lis[ i ], lis[ j ] +1 )
    k =  np.argmax( lis )
    ns = [ ss[k] ]
    i = k
    for j in xrange( k-1,-1,-1 ):
        if lis[ j ] == lis[ i ] -1 and ss[ j ] < ss[ i ] :
            ns.append( ss[j] )
            i = j
    ns.reverse()
    return ns
 
def get_lds( ss ):  # Longest decreasing subsequence
    import numpy as np
    lis = [ 1 ]*len(ss)
    for i in xrange( 1, len(ss)):
        for j in xrange( 0, i ):
            if ss[ i ] < ss[ j ]:
                lis[ i ] = max( lis[ i ], lis[ j ] +1 )
    k =  np.argmax( lis )
    ns = [ ss[k] ]
    i = k
    for j in xrange( k-1,-1,-1 ):
        if lis[ j ] == lis[ i ] -1 and ss[ j ] > ss[ i ] :
            ns.append( ss[j] )
            i = j
    ns.reverse()
    return ns
 
print " ".join(map(str,get_lis( ss )))
print " ".join(map(str,get_lds( ss )))


inc = [(0,[])]*(n+1)

for i in l:
    x,y = max(inc[:i])
    inc[i] = (x+1,y+[i])