def RemoveCols(A, K1, K2):
    M = len(A)
    if M == 0:
        return A
    N = len(A[0])
    
    if K1 > N:
        return A
    
    end_col = min(K2, N)
    
    result = []
    for i in range(M):
        new_row = []
        for j in range(N):
            if j < K1 - 1 or j >= end_col:
                new_row.append(A[i][j])
        result.append(new_row)
    
    return result
