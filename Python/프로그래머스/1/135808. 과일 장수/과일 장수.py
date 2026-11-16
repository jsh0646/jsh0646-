def solution(k, m, score):
    answer = 0
    box = len(score) // m
    score.sort()
    for x in range(box):
        lst = []
        for y in range(m):
            lst.append(score.pop())
        answer += m*lst[-1]
    return answer