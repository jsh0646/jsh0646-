def solution(sizes):
    long = []
    short = []
    for l in sizes:
        long.append(max(l))
        short.append(min(l))
    return max(long) * max(short)