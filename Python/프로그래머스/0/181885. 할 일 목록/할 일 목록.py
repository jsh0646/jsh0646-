def solution(todo_list, finished):
    answere = []
    for i in range(len(todo_list)):
        if finished[i] != True:
            answere.append(todo_list[i])
    return answere
            