def solution(emergency):
    sort_e = sorted(emergency, reverse = True)
    rank = {}
    for i,x in enumerate(sort_e, start=1):
        rank[x]=i
    
    ans = []
    for e in emergency:
        ans.append(rank[e])
    return ans