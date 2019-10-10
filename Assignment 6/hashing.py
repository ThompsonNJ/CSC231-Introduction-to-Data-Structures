import math

def o0o0o0o0o0o0o0o(oo0o0o0o0o0o0o0o):
    return int(math.log10(oo0o0o0o0o0o0o0o))

def secret_hash(l1l1l1l1l1l1111, l1l1l1l1l1l1111lll):
    l1l1l1l1l1l1=o0o0o0o0o0o0o0o(l1l1l1l1l1l1111lll)
    l1l1l1l1l1l1l1=str(int(l1l1l1l1l1l1111.replace('-',''))**2)
    l1l1l1l1l1l1l=len(l1l1l1l1l1l1l1)//2-l1l1l1l1l1l1//2
    l1l1l1l1l1l11=''
    for i in range(l1l1l1l1l1l1):
        l1l1l1l1l1l11+=l1l1l1l1l1l1l1[l1l1l1l1l1l1l+i]
    return int(l1l1l1l1l1l11)%l1l1l1l1l1l1111lll