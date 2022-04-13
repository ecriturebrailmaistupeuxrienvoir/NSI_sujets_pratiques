def moyenne(notes : list) -> float :
    acc_coef = 0
    acc_notes = 0
    for i in range (len(notes)) :
        acc_coef += notes[i][1]
        acc_notes += notes[i][0] * notes[i][1]
    return acc_notes / acc_coef
    
def pascal(n):
    C= [[1]]
    for k in range(1, n + 1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
