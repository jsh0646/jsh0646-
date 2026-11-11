def solution(players, callings):
    #이름 등수 딕셔너리
    rank = {}
    for i,p in enumerate(players):
        rank[p] = i
        
    for call in callings:
        k = rank[call]
        
        prev = players[k-1]
        players[k],players[k-1] = players[k-1],players[k]
        #rank 등수 수정
        rank[call] = k-1
        rank[prev] = k
        
    return players