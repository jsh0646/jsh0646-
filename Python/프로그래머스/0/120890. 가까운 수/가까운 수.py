def solution(array, n):
    #기준1.n과 가장 가까운 수
    #기준2.거리가 같으면 작은 수
    array.sort(key = lambda x: (abs(x-n),x))
    return array[0]