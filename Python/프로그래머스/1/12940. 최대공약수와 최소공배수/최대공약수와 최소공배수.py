def solution(n, m):
    lcm = n * m
    while m > 0:
        n,m = m , n % m
    gcd = n
    lcm //= gcd
    return[gcd,lcm]