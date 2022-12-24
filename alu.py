from utils import *

def a74181(S,M,Cn,Ab,Bb):
    A = copy.deepcopy(Ab)
    B = copy.deepcopy(Bb)
    Sv = S[0]*8+S[1]*4+S[2]*2+S[3]
    cry = 0
    one = [0,0,0,1]
    F = [0,0,0,0]

    if (Sv == 0):
        if (M == 1):
            F = c1(A)
        else:
            if (Cn == 0):
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = s1(A[k],one,cry)
            else:
                F = copy.deepcopy(A)
    elif (Sv == 1):
        if (M == 1):
            for k in range(4):
                F[k] = A[k] & B[k]
                c1(F)
        else:
            if (Cn == 0):
                for k in range(4):
                    F[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = s1(F[k],one,cry)
            else:
                for k in range(4):
                    F[k] = A[k] & B[k]
    elif (Sv == 2):
        if (M == 1):
            F = c1(A)
            for k in range(4):
                F[k] = F[k] | B[k]
        else:
            if (Cn == 0):
                F = c1(B)
                for k in range(4):
                    F[k] = A[k] & F[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = s1(F[k],one,cry)
            else:
                F = c1(B)
                for k in range(4):
                    F[k] = A[k] & F[k]
    elif (Sv == 3):
        if (M == 1):
            F = [1,1,1,1]
        else:
            if (Cn == 0):
                F = [1,1,1,1]
            else:
                F = [0,0,0,0]
    elif (Sv == 4):
        if (M == 1):
            for k in range(4):
                F[k] = A[k] | B[k]
            c1(F)
        else:
            if (Cn == 0):
                F = c1(B)
                for k in range(4):
                    F[k] = A[k] | F[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
            else:
                F = c1(B)
                for k in range(4):
                    F[k] = A[k] | F[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 5):
        if (M == 1):
            F = c1(B)
        else:
            if (Cn == 0):
                F = c1(B)
                for k in range(4):
                    F[k] = A[k] | F[k]
                for k in range(4):
                    A[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
            else:
                F = c1(B)
                for k in range(4):
                    F[k] = A[k] | F[k]
                for k in range(4):
                    A[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 6):
        if (M == 1):
            for k in range(4):
                F[k] = A[k] ^ F[k]
            c1(F)
        else:
            if (Cn == 0):
                for k in range(3,-1,-1):
                    (F[k],cry) = s1(A[k],B[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = s1(F[k],one,cry)
            else:
                for k in range(3,-1,-1):
                    (F[k],cry) = s1(A[k],B[k],cry)
    elif (Sv == 7):
        if (M == 1):
            c1(B)
            for k in range(4):
                F[k] = A[k] | B[k]
        else:
            if (Cn == 0):
                c1(B)
                for k in range(4):
                    F[k] = A[k] | B[k]
            else:
                c1(B)
                for k in range(4):
                    F[k] = A[k] | B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 8):
        if (M == 1):
            c1(A)
            for k in range(4):
                F[k] = A[k] & B[k]
        else:
            if (Cn == 0):
                for k in range(4):
                    F[k] = A[k] | B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
            else:
                for k in range(4):
                    F[k] = A[k] | B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 9):
        if (M == 1):
            for k in range(4):
                F[k] = A[k] ^ B[k]
        else:
            if (Cn == 0):
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],B[k],cry)
            else:
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],B[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 10):
        if (M == 1):
            F = copy.deepcopy(B)
        else:
            if (Cn == 0):
                for k in range(4):
                    F[k] = A[k] | B[k]
                c1(B)
                for k in range(4):
                    A[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
            else:
                for k in range(4):
                    F[k] = A[k] | B[k]
                c1(B)
                for k in range(4):
                    A[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],F[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 11):
        if (M == 1):
            for k in range(4):
                F[k] = A[k] | B[k]
        else:
            if (Cn == 0):
                for k in range(4):
                    F[k] = A[k] | B[k]
            else:
                for k in range(4):
                    F[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 12):
        if (M == 1):
            F = [0,0,0,0]
        else:
            if (Cn == 0):
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],A[k],cry)
            else:
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],A[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 13):
        if (M == 1):
            c1(B)
            for k in range(4):
                F[k] = A[k] & B[k]
        else:
            if (Cn == 0):
                for k in range(4):
                    F[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],A[k],cry)
            else:
                for k in range(4):
                    F[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],A[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 14):
        if (M == 1):
            for k in range(4):
                F[k] = A[k] & B[k]
        else:
            if (Cn == 0):
                c1(B)
                for k in range(4):
                    F[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],A[k],cry)
            else:
                c1(B)
                for k in range(4):
                    F[k] = A[k] & B[k]
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],A[k],cry)
                cry = 0
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(F[k],one,cry)
    elif (Sv == 15):
        if (M == 1):
            F = copy.deepcopy(A)
        else:
            if (Cn == 0):
                F = copy.deepcopy(A)
            else:
                for k in range(3,-1,-1):
                    (F[k],cry) = a1(A[k],one,cry)

    return F