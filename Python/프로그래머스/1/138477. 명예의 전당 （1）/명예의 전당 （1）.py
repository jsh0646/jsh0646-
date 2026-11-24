def solution(k, score):
    answer = []
    x = []
    for i in score:
        if len(answer) < k:
            answer.append(i)
        else:
            if i > min(answer):
                answer.remove(min(answer))
                answer.append(i)
        x.append(min(answer))
    return x