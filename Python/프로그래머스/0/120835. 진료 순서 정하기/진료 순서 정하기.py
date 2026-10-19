def solution(emergency):
    lst = []
    for x in emergency:
        num = 1
        for y in emergency:
            if x < y:
                num+=1
        lst.append(num)
    return lst
        