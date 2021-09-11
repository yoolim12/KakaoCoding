def solution(board, skill):
    cnt = 0
    for e in skill:
        wtype, r1, c1, r2, c2, deg = e
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if wtype == 1:
                    board[row][col] -= deg
                else:
                    board[row][col] += deg
    
    for e in board:
        res = list(filter(lambda x: x if x > 0 else '', e))
        cnt += len(res)

    answer = cnt
    return answer

print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))