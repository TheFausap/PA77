from utils import *
import math
from decimal import Decimal as Dec
from decimal import getcontext

MEM = [[0 for i in range(21)] for j in range(8192)]

AC = [0 for i in range(42)]
MQ = [0 for i in range(42)]
EXR7 = [0 for i in range(42)]
LR = [0 for i in range(12)]
XR6 = MEM[5]
XR7 = MEM[6]

def xprint(b):
    print("[0,............................1,............................2]")
    print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]")
    print(b,sep='')

def pprint(ad,f=0):
    if (tag(MEM[ad]) == 0):
        m = get(MEM[ad],16,17)
        s = '' if (MEM[ad][3]==0) else '-'
        v = 0
        if (s == '-'):
            c1(m)
        if (f == 0):
            v = int(tostr(m),2)
        elif (f == 2):
            v = intf(tostr(m))
        elif (f == 1):
            v = 1+intf(tostr(m))
        print(s,v,sep='')
    elif (tag(MEM[ad]) == 2):
        ade = int(gets(MEM[ad],17,9),2)
        adm = int(gets(MEM[ad],8,9),2)
        pprint(adm,f=2)
        pprint(ade)
    elif (tag(MEM[ad]) == 1):
        ade = int(gets(MEM[ad],17,9),2)
        adm = int(gets(MEM[ad],8,9),2)
        pprint(adm,f=1)
        pprint(ade)
        
def normal(ad):
    ade = int(gets(MEM[ad],17,9),2)
    adm = int(gets(MEM[ad],8,9),2)
    mb = MEM[adm][4:]
    de = 1
    exb = MEM[ade][4:]
    sm = MEM[adm][3]
    se = MEM[ade][3]
    if (sm == 1):
        c1(mb)
    while(mb[0] != 1):
        mb = shl(mb)
        de += 1
    mb = shl(mb)
    if (sm == 1):
        c1(mb)
    set(MEM[adm],mb,16,17)
    re = int(tostr(exb),2) if (se == 0) else -1*int(tostr(c1(exb)),2)
    re -= de
    exb = tobin(re,17)
    if (re < 0):
        c1(exb)
        set(MEM[ade],[1],17,1)
    set(MEM[ade],exb,16,17)
    set(MEM[ad],[0,0,1],20,3)
    
def fsetv(ad,adf,v):
    i = 0
    j = 0
    s = 0
    se = 0
    if (v < 0):
        s = 1
        v = abs(v)
    vint = int(v)
    nd = 0 if (vint == 0) else int(math.log10(vint)/math.log10(2))
    bint = [0 for i in range(nd+1)]
    vdec = Dec(v) - vint
    i = nd
    while(vint != 0):
        bint[i] = vint % 2
        i -= 1
        vint //= 2
        j += 1
    i = 0
    bdec = [0 for i in range(17-j)]
    while(j<17):
        vdec *= 2
        bdec[i] = int(vdec)
        j += 1
        i += 1
        vdec -= int(vdec)
    
    if ((s==0) and (int(v) != 0)):
        exp = len(bint)
        expb = tobin(exp,17)
        mant = bint+bdec
    elif ((s==0) and (int(v) == 0)):
        exp = 0
        expb = tobin(exp,17)
        mant = bdec
    elif ((s==1) and (int(v) != 0)):
        exp = len(bint)
        expb = tobin(exp,17)
        mant = bint+bdec
        c1(mant)
    elif ((s==1) and (int(v) == 0)):
        exp = 0
        expb = tobin(exp,17)
        mant = bdec
        c1(mant)
    set(MEM[ad],[0,1,0],20,3)
    set(MEM[adf],[0,0,0],20,3)
    set(MEM[adf+1],[0,0,0],20,3)
    set(MEM[ad],tobin(adf,9),17,9)
    set(MEM[ad],tobin(adf+1,9),8,9)
    set(MEM[adf],expb,16,17)
    set(MEM[adf+1],[s],17,1)
    set(MEM[adf+1],mant,16,17)
    
### TESTS

fsetv(100,110,67.35)

xprint(MEM[100])
xprint(MEM[110])
xprint(MEM[111])

pprint(100)

normal(100)
xprint(MEM[110])
xprint(MEM[111])

pprint(100)
