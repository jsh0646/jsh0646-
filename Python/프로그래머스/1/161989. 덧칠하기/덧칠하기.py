def solution(n, m, section):
    answer = 0
    paint = 0
    for k in section:
        if k > paint:
            paint = k + m - 1
            answer += 1
        
    return answer