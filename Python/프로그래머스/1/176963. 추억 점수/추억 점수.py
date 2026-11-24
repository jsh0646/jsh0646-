def solution(name, yearning, photo):
    answer = []
    scr_d = dict(zip(name,yearning))
    for l in photo:
        total = 0
        for x in l:
            if x in scr_d:
                total += scr_d[x]
        answer.append(total)
    return answer