from utils import *
from alu import a74181
import math
from decimal import Decimal as Dec
from decimal import getcontext
import random

MEM = [[0 for i in range(21)] for j in range(8192)]

PC = MEM[0]
MEM[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
R0 = MEM[2]
R1 = MEM[3]

def init():
    for b in MEM:
        set(b,[1,1,1],20,3)
        
def gaddr():
    ad = random.randint(32,511)
    if (gets(MEM[ad],20,3) != '111'):
        gaddr()
    return ad
        
def xprint(b):
    print("[0,............................1,............................2]")
    print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]")
    print(b,sep='')

def pprint(ad,f=0):
    if (tag(MEM[ad]) == 0):
        m = get(MEM[ad],16,17)
        s = '' if (MEM[ad][3]==0) else '-'
        v = 0
        if (f == 0):
            v = int(tostr(m),2)
        elif (f == 2):
            v = intf(m)
        elif (f == 1):
            v = 1+intf(m)
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
    #if (sm == 1):
        #c1(mb)
    while(mb[0] != 1):
        mb = shl(mb)
        de += 1
    mb = shl(mb)
    #if (sm == 1):
        #c1(mb)
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
        #c1(mant)
    elif ((s==1) and (int(v) == 0)):
        exp = 0
        expb = tobin(exp,17)
        mant = bdec
        #c1(mant)
    set(MEM[ad],[0,1,0],20,3)
    set(MEM[adf],[0,0,0],20,3)
    set(MEM[adf+1],[0,0,0],20,3)
    set(MEM[ad],tobin(adf,9),17,9)
    set(MEM[ad],tobin(adf+1,9),8,9)
    set(MEM[adf],expb,16,17)
    set(MEM[adf+1],[s],17,1)
    set(MEM[adf+1],mant,16,17)
        
def addf(d,d1,d2,ad1,ad2,cry=0):
    ade1 = int(gets(MEM[ad1],17,9),2)
    adm1 = int(gets(MEM[ad1],8,9),2)
    ade2 = int(gets(MEM[ad2],17,9),2)
    adm2 = int(gets(MEM[ad2],8,9),2)
    se1 = MEM[ade1][3]
    sm1 = MEM[adm1][3]
    ex1 = int(gets(MEM[ade1],16,17),2) if (se1 == 0) else -1*int(tostr(c1(get(MEM[ade1],16,17))),2)
    m1 = get(MEM[adm1],16,17) # mantissa
    m1 = [1] + m1
    se2 = MEM[ade2][3]
    sm2 = MEM[adm2][3]
    ex2 = int(gets(MEM[ade2],16,17),2) if (se2 == 0) else -1*int(tostr(c1(get(MEM[ade2],16,17))),2)
    m2 = get(MEM[adm2],16,17) # mantissa
    m2 = [1] + m2
    ex = ex1
    if (ex1 > ex2):
        while (ex2 < ex1):
            m2 = shr(m2)
            ex2 += 1
    elif (ex1 < ex2):
        while (ex1 < ex2):
            m1 = shr(m1)
            ex1 += 1
        ex = ex2
    # addition of mantissa
    lm = len(m1)
    m3 = [0 for k in range(lm)]
    z = [0 for k in range(lm)]
    s = 0
    for y in range(lm-1,-1,-1):
        (m3[y],cry) = a1(m1[y],m2[y],cry)
    if ((sm1 == 1) and (sm2 == 1)):
        if (cry == 1):
            for y in range(lm-1,-1,-1):
                (m3[y],cry) = a1(m3[y],z[y],cry)
        s = 1
    if (cry == 1):
    # overflow into hidden bit
        m3 = shr(m3)
        ex += 1
        m3[0] = 1
    
    h = m3[0]
    m = m3[1:]
    set(MEM[d],[0,1,0],20,3)
    set(MEM[d1],[0,0,0],20,3)
    set(MEM[d2],[0,0,0],20,3)
    set(MEM[d],tobin(d1,9),17,9)
    set(MEM[d],tobin(d2,9),8,9)
    set(MEM[d2],[s],17,1)
    set(MEM[d2],m,16,17)
    set(MEM[d1],tobin(ex,17),16,17)
    
    if (h == 0):
        normal(d)
    set(MEM[d],[0,0,1],20,3)
    
def subf(d,d1,d2,ad1,ad2,cry=0):
    ade1 = int(gets(MEM[ad1],17,9),2)
    adm1 = int(gets(MEM[ad1],8,9),2)
    ade2 = int(gets(MEM[ad2],17,9),2)
    adm2 = int(gets(MEM[ad2],8,9),2)
    se1 = MEM[ade1][3]
    se2 = MEM[ade2][3]
    sm1 = MEM[adm1][3]
    ex1 = int(gets(MEM[ade1],16,17),2) if (se1 == 0) else -1*int(tostr(c1(get(MEM[ade1],16,17))),2)
    ex2 = int(gets(MEM[ade2],16,17),2) if (se2 == 0) else -1*int(tostr(c1(get(MEM[ade2],16,17))),2)
    m1 = get(MEM[adm1],16,17) # mantissa
    m2 = get(MEM[adm2],16,17) # mantissa
    if ((1+intf(m1))*2**ex1 > (1+intf(m2))*2**ex2):
        s = 0
        m1b = 1
    elif ((1+intf(m1))*2**ex1 < (1+intf(m2))*2**ex2):
        s = 1
        m1b = 0
    else:
        s = 0
    m1 = [1] + m1
    
    sm2 = MEM[adm2][3]
    
    m2 = [1] + m2
    ex = ex1
    if (ex1 > ex2):
        while (ex2 < ex1):
            m2 = shr(m2)
            ex2 += 1
    elif (ex1 < ex2):
        while (ex1 < ex2):
            m1 = shr(m1)
            ex1 += 1
        ex = ex2
    # subtraction of mantissa
    lm = len(m1)
    m3 = [0 for k in range(lm)]
    z = [0 for k in range(lm)]
    
    for y in range(lm-1,-1,-1):
        (m3[y],cry) = s1(m1[y],m2[y],cry)
    
    if (m3[0] == 0):
        # underflow
        l0 = ldzero(m3)
        while (l0 > 0):
            m3 = shl(m3)
            ex -= 1
            l0 -= 1
        m3[0] = 1
    
    h = m3[0]
    m = m3[1:]
    set(MEM[d],[0,1,0],20,3)
    set(MEM[d1],[0,0,0],20,3)
    set(MEM[d2],[0,0,0],20,3)
    set(MEM[d],tobin(d1,9),17,9)
    set(MEM[d],tobin(d2,9),8,9)
    set(MEM[d2],[s],17,1)
    set(MEM[d2],m,16,17)
    set(MEM[d1],tobin(ex,17),16,17)
    
    if (h == 0):
        normal(d)
    set(MEM[d],[0,0,1],20,3)
    
def ADD(d,ad1,ad2,cry=0):
    adm1 = int(gets(MEM[ad1],8,9),2)
    adm2 = int(gets(MEM[ad2],8,9),2)
    sm1 = MEM[adm1][3]
    sm2 = MEM[adm2][3]
    d1 = gaddr()
    d2 = gaddr()
    if (sm1 == sm2):
        addf(d,d1,d2,ad1,ad2,cry=0)
    else:
        subf(d,d1,d2,ad1,ad2,cry=0)
        
def SUB(d,ad1,ad2,cry=0):
    adm1 = int(gets(MEM[ad1],8,9),2)
    adm2 = int(gets(MEM[ad2],8,9),2)
    sm1 = MEM[adm1][3]
    sm2 = MEM[adm2][3]
    d1 = gaddr()
    d2 = gaddr()
    if (sm1 != sm2):
        addf(d,d1,d2,ad1,ad2,cry=0)
    else:
        subf(d,d1,d2,ad1,ad2,cry=0)
        
def idiv(ad1,ad2):
    n = get(MEM[ad1],16,17) 
    d = get(MEM[ad2],16,17)
    sn = MEM[ad1][3]
    sd = MEM[ad2][3]
    one = get(MEM[1],16,17)
    cry = 0
    q = [0 for k in range(len(n))]
    t = [0 for k in range(len(n))]
    w = copy.deepcopy(n)
    ld1 = ldzero(n)
    ld2 = ldzero(d)
    if (ld1 > ld2):
        return
    elif (ld1 < ld2):
        un = ld2-ld1
        for i in range(un):
            d = shl(d)
    else:
        un = 0
    k = un
    lw1 = len(n) - ld1
    while (k>=0):
        cry = 0
        q = shl(q)
        for y in range(len(n)-1,(len(n)-1)-lw1,-1):
            (t[y], cry) = s1(w[y],d[y],cry)
        if (cry == 0):
            q[-1] = 1
            w = copy.deepcopy(t)
        k -= 1
        d = shr(d)
    if (sn == sd):
        set(MEM[ad1],[0],17,1)
    else:
        set(MEM[ad1],[1],17,1)
    set(MEM[ad1],[0,0,0],20,3)
    set(MEM[ad1],q,16,17)
    set(MEM[2],[0,0,0],20,3)
    set(MEM[2],w,16,17)

def imul(ad1,ad2):
    m1 = get(MEM[ad1],16,17) 
    m2 = get(MEM[ad2],16,17)
    sn = MEM[ad1][3]
    sd = MEM[ad2][3]
    
    cry = 0
    ld1 = ldzero(m1)
    ld2 = ldzero(m2)
    lw1 = len(m1) - ld1
    lw2 = len(m2) - ld2
    lw = lw1 if (lw1 > lw2) else lw2
    mlpr = [0 for k in range(lw)]
    mlpd = [0 for k in range(lw)]
    t = [0 for k in range(lw)]
    mlpr[lw-lw2:]=m2[ld2:]
    mlpd[:]=m1[ld1:]
    q = copy.deepcopy(mlpr)
    k = lw
    while (k>0):
        if (q[-1] == 1):
            for y in range(len(q)-1,-1,-1):
                (t[y], cry) = a1(t[y],mlpd[y],cry)
            q = shr(q)
            q[0] = t[-1]
            t = shr(t)
            t[0] = cry
            cry = 0
        else:
            q = shr(q)
            q[0] = t[-1]
            t = shr(t)
            t[0] = cry
            cry = 0
        k -= 1
    xprint(t)
    xprint(q)
    
### TESTS

init()

fsetv(100,110,-9)
fsetv(101,115,-3)

print('Before normalization a1')
xprint(MEM[110])
xprint(MEM[111])

normal(100)
normal(101)

print('After normalization a1')
xprint(MEM[110])
xprint(MEM[111])
pprint(100)

print('After normalization a2')
xprint(MEM[115])
xprint(MEM[116])
pprint(101)

print('Addition')
ADD(105,100,101)
#xprint(MEM[120])
#xprint(MEM[121])
pprint(105)

#set(MEM[1000],tobin(-12,17),16,17)
#set(MEM[1001],tobin(5,17),16,17)
setv(MEM[1000],12)
setv(MEM[1001],2)

#idiv(1000,1001)
#xprint(MEM[1000])
#pprint(1000)
#xprint(R0)
#pprint(2)

imul(1000,1001)
