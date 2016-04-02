def mul(A, B, mb, me, anb, ane, bnb, bne, pb, pe, C):
    """A is m × n matrix, B is n × p matrix
    mb: beginning index of m, me: ending index of m
    anb: beginning index of vertical of A, ane: ending index of vetical of A
    bnb: beginning index of horizontal of B, bne: ending index of horizontal of B
    pb: beginning index of p, pe: ending index of p
    need to initialize C to a m × p matrix with zeros"""
    an = ane - anb + 1
    bn = bne - bnb + 1
    if an != bn:
        return None
    n = an
    m = me - mb + 1
    p = pe - pb + 1
    if n == m == p == 1:
        C[mb][pb] += A[mb][anb] * B[bnb][pb]
    elif max(m, n, p) == m:
        # split A horizontally
        mid = (mb + me) // 2
        mul(A, B, mb, mid, anb, ane, bnb, bne, pb, pe, C)
        mul(A, B, mid + 1, me, anb, ane, bnb, bne, pb, pe, C)
    elif max(m, n, p) == p:
        # split B vertically
        mid = (pb + pe) // 2
        mul(A, B, mb, me, anb, ane, bnb, bne, pb, mid, C)
        mul(A, B, mb, me, anb, ane, bnb, bne, mid + 1, pe, C)
    else:
        # split A vertically and B horizontally
        amid = (anb + ane) // 2
        bmid = (bnb + bne) // 2
        mul(A, B, mb, me, anb, amid, bnb, bmid, pb, pe, C)
        mul(A, B, mb, me, amid + 1, ane, bmid + 1, bne, pb, pe, C)


A = [[1,2,3], [2,4,5], [3,2,7]]
B = [[4,7,5], [2,8,1], [3,6,9]]
row = len(A)
col = len(B[0])
C = []
for i in range(row):
    C.append([])
    for j in range(col):
        C[i].append(0)
print(C)
mul(A, B, 0, len(A) - 1, 0, len(A[0]) - 1, 0, len(B) - 1, 0, len(B[0]) - 1, C)
print(C)
