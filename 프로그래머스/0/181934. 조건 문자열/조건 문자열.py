def solution(ineq, eq, n, m):
    if ineq == ">":
        result = (n >= m) if eq == "=" else (n > m)
    else:
        result = (n <= m) if eq == "=" else (n < m)
    return int(result)