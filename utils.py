import copy
import math

#            0     1     2    3    4    5    6    7    8    9
sqz2char = [' ' , '0' , '1', '2', '3', '4', '5', '6', '7', '8', # 0
            '9',  'A' , 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', # 1
            'J',  'K',  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', # 2
            'T',  'U',  'V', 'W', 'X', 'Y', 'Z', '=', '|', ')', # 3
            '+',  '-',  '^', '<', '>', '*', '/', '$', ',', '.', # 4
            ';',  '(',  '{', '_',  0 ,'\\','\'', '`', '~',  0 , # 5
             0 ,   0 ,   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , # 6
             0 ,   0 ,   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , # 7
             0 ,   0 ,   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , # 8
             0 ,   0 ,   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , '#', # 9
            '%',  ']',  '&',  0 , '@', '?', ':',  0 ,  0 ,  0 , # 10
             0 ,   0 ,   0 , '[', '}', '!',  0 ,  0 ,  0 , '"', # 11
             0 ,   0 ,   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , # 12
             0 ,   0 ,   0 ,  0 ,  0 ,  0 ,  0 , 'a', 'b', 'c', # 13
            'd',  'e',  'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', # 14
            'n',  'o',  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', # 15
            'x',  'y',  'z',  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , # 16
             0 ,   0 ,   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , # 17
             0]

#            0    1    2    3    4    5    6    7    8    9
char2sqz = [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,    # 0
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,    # 1
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,    # 2
             0,   0,   0,   115, 119, 99,  47,  100, 102, 56,   # 3
             51,  39,  45,  40,  48,  41,  49,  46,  1,   2,    # 4
             2,   3,   4,   5,   6,   7,   8,   9,   106, 50,   # 5
             43,  37,  44,  105, 104, 11,  12,  13,  14,  15,   # 6
             16,  17,  18,  19,  20,  21,  22,  23,  24,  25,   # 7
             26,  27,  28,  29,  30,  31,  32,  33,  34,  35,   # 8
             36,  113, 55,  101, 42,  53,  57,  137, 138, 139,  # 9
             140, 141, 142, 143, 144, 145, 146, 147, 148, 149,  # 10
             150, 151, 152, 153, 154, 155, 156, 157, 158, 159,  # 11
             160, 161, 162, 52,  38,  114, 58 ]                 # 12

def twrite(f,s):
    for c in s:
        c_enc = chr(char2sqz[ord(c)]+35)
        EOL = chr(char2sqz[ord('\\')]+35)
        f.write(c_enc.encode())
    f.write(EOL.encode())

def tend(f):
    EOL = chr(char2sqz[ord('|')]+35)
    f.write(EOL.encode())

def tread(f):
    c_enc = f.read(1).decode()
    if (c_enc != ''):
        c_dec = ord(c_enc)-35
        c_enc = sqz2char[c_dec]
    return c_enc

def set(b,v,s,nb):
    bb = len(b) - 1
    s = bb - s
    b[s:s+nb] = v

def get(b,s,nb):
    bb = len(b) - 1
    s = bb - s
    return b[s:s+nb]

def gets(b,s,nb):
    bb = len(b) - 1
    s = bb - s
    return ''.join(str(k) for k in b[s:s+nb])

def tostr(b):
    return ''.join(str(k) for k in b)

def _intf(s):
    return int(s, 2) / 2.**(len(s))

def intf(s):
    j = -1
    r = 0
    for b in s:
        r += b * 2**j
        j -= 1
    return r
    
def zero(b):
    for y in range(len(b)):
        b[y] = 0
        
def sum(b):
    r = 0
    for i in b:
        r += i
    return r

def ldzero(b):
    r = 0
    for y in range(len(b)):
        if (b[y] == 0):
            r += 1
        else:
            return r

# how many 1 are in the number
def ones(b):
    r = 0
    for y in range(len(b)):
        if (b[y] == 1):
            r += 1
    return r

# converts the absolute value of v into binary of length p
def tobin(v,p):
    v = abs(v)
    nd = 0 if (v == 0) else int(math.log10(v)/math.log10(2))
    nd = nd if (p < nd) else p-1
    b = [0 for y in range(nd+1)]
    if (v == 0):
        return b
    i = nd
    while (v != 0):
        b[i] = v % 2
        i -= 1
        v //= 2
    return b
    
def c1(b):
    for y in range(len(b)):
        if (b[y] == 0):
            b[y] = 1
        else:
            b[y] = 0
    return b

def tag(b):
    return b[0]*4+b[1]*2+b[2]

def pdump(b):
    ts = ''.join([str(item) for item in b])
    print(ts, int(ts,2))
    
def setv(b,v):
    i = len(b) - 1
    s = 0
    if (v < 0):
        s = 1
        v = abs(v)
    while (v != 0):
        b[i] = v % 2
        v = v // 2
        i -= 1
    if (s == 1):
        c1(b)
        
def a1(b1,b2,c):
    r = b1+b2+c
    if r > 2:
        r = 1
        c = 1
    elif r > 1:
        r = 0
        c = 1
    else:
        c = 0
    return (r,c)

def s1(b1,b2,c):
    r = (b1-b2)-c
    if r < -1:
        r = 0
        c = 1
    elif r < 0:
        r = 1
        c = 1
    else:
        c = 0
    return (r,c)
    
# integer addition used in floating point add
# sign in the first position (0)
# hidden bit is the second position (1)
# returns the addition
def addi(ba1,ba2,cry=0):
    l1 = len(ba1)
    l2 = len(ba2)
    if (l1 < l2):
        ba1 = [0 for k in range(l2-l1)] + ba1
    elif (l1 > l2):
        ba2 = [0 for k in range(l1-l2)] + ba2
    r = [0 for k in range(l1)]
    z = [0 for k in range(l1)]
    if (ba1[0] != ba2[0]):
        for y in range(l1-1,-1,-1):
            (r[y],cry) = a1(ba2[y],ba1[y],cry)
        if (cry == 1):
            for y in range(l1-1,-1,-1):
                (r[y],cry) = a1(r[y],z[y],cry)
    else:
        for y in range(l1-1,-1,-1):
            (r[y],cry) = a1(ba1[y],ba2[y],cry)
        if (ba1[0] != ba2[0]):
            if (cry == 1):
                print("addi UND")
            else:
                print("addi OVR")
        else:
            if (cry == 1):
                for y in range(l1-1,-1,-1):
                    (r[y],cry) = a1(r[y],z[y],cry)
    return (r[0],r[1],r[2:])

def addi2(ba1,ba2,cry=0):
    l1 = len(ba1)
    l2 = len(ba2)
    if (l1 < l2):
        ba1 = [0 for k in range(l2-l1)] + ba1
    elif (l1 > l2):
        ba2 = [0 for k in range(l1-l2)] + ba2
    r = [0 for k in range(l1)]
    z = [0 for k in range(l1)]
    if (ba1[0] != ba2[0]):
        for y in range(l1-1,-1,-1):
            (r[y],cry) = a1(ba2[y],ba1[y],cry)
        if (cry == 1):
            for y in range(l1-1,-1,-1):
                (r[y],cry) = a1(r[y],z[y],cry)
    else:
        for y in range(l1-1,-1,-1):
            (r[y],cry) = a1(ba1[y],ba2[y],cry)
        if (ba1[0] != ba2[0]):
            if (cry == 1):
                print("addi UND")
            else:
                print("addi OVR")
        else:
            if (cry == 1):
                for y in range(l1-1,-1,-1):
                    (r[y],cry) = a1(r[y],z[y],cry)
    return (r[0],r[1],r[2:])

def shl(b):
    bb = copy.deepcopy(b)
    bb.append(bb.pop(0))
    bb[-1] = 0
    return bb

def shr(b):
    bb = copy.deepcopy(b)
    bb.insert(0,bb.pop())
    bb[0] = 0
    return bb

def rol(b,n=1):
    t = b[n:] + b[:n]
    for y in range(len(b)):
        b[y] = t[y]

def ror(b,n=1):
    t = b[-n:] + b[:-n]
    for y in range(len(b)):
        b[y] = t[y]
        
