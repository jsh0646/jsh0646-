def solution(board):
    n = len(board) #보드는 n*n
    danger_set = set() # 위험지역 집합
    
    # 지뢰 찾기 및 위험지역 찾아 위험지역 집합에 저장
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1: # 지뢰 위치
                for dr in (-1,0,1):
                    for dc in (-1,0,1):
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < n and 0 <= new_c < n:
                            danger_set.add((new_r,new_c))
                
    return n*n - len(list(danger_set))