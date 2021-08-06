if __name__ == "__main__":

    n = 20

    mat = [["" for _ in range(n)] for _ in range(n) ]
    i = len(mat[0])-1
    j_start = len(mat)//2
    j_end = len(mat)//2

    while(j_start >= 0 and j_end < len(mat[0])):
        mat[i][j_start] = "*"
        mat[i][j_end] = "*"
        i -= 1
        j_start -= 1
        j_end += 1

    mat[i+1][len(mat[0])//2] = "*"

    mid_start = len(mat[0])//2 
    mid_end = mid_start

    j_start = 0;j_end = len(mat[0])-1

    while(i>=0):
        mat[i][j_start] = "*"
        mat[i][j_end] = "*"
        mat[i][mid_start] = "*"
        mat[i][mid_end] = "*"

        j_start += 1
        j_end -= 1
        mid_start -= 1
        mid_end += 1
        i -= 1
        

    
    for i in range(n):
        if i == 1:
            continue
        print(*mat[i])
