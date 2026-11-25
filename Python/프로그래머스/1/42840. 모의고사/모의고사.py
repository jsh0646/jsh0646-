def solution(answers):
    patern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]] 
    n_correct = []# 맟힌 문제 수
    for p in patern:
        score = 0
        for i in range(len(answers)):
            if p[i % len(p)] == answers[i]:
                score += 1
        n_correct.append(score)
    max_score = max(n_correct)
    answer = []
    for i in range(3):
        if n_correct[i] == max_score:
            answer.append(i + 1)
    return answer