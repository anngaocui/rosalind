def mian():
    tree = open('/home/ralf/Downloads/rosalind_mend.txt').readline().split(";")[0]
    dic = {"AA": [1, 0, 0], "Aa": [0, 1, 0], "aa": [0, 0, 1]}
    kk, p, q = [], [], []
    for j in tree.replace("(", "").replace(")", "").split(","):
        kk.append(dic[j])
    m = 0
    g = ''
    for i in tree:
        if i == "(" or i == ")" or i == ",":
            if g != "":
                q.append(p)
                g = ''
            if i == "(":
                m = m + 1
                p.append(m)
            elif i == ")":
                p = p[:-1]
        else:
            g = g + i
    while len(kk) > 2:
        q, kk = mend(kk, q)
    a = child2(kk[1], kk[0])
    print a


def child2(l1, l2):
    AA = l1[0] * l2[0] + 0.5 * (l1[0] * l2[1] + l2[0] * l1[1]) + 0.25 * (l1[1] * l2[1])
    aa = l1[2] * l2[2] + 0.5 * (l1[1] * l2[2] + l1[2] * l2[1]) + 0.25 * (l1[1] * l2[1])
    Aa = 1 - aa - AA
    return [AA, Aa, aa]


def mend(kk, q):
    l1, l2 = [], []
    m = -1
    for i in range(len(kk)):
        if i == m:
            continue
        else:
            if i < len(kk) - 1 and q[i] == q[i + 1]:
                p = child2(kk[i], kk[i + 1])
                l1.append(q[i][:-1])
                l2.append(p)
                m = i + 1
            else:
                l1.append(q[i])
                l2.append(kk[i])
    return (l1, l2)
