def count_one(n, x):
    if n == 0:
        return 1
    if x <= 0:
        return 0
    
    unit = 5 ** (n - 1)
    
    zone = (x - 1) // unit
    remainder = (x - 1) % unit
    
    one_in_prev = 4 ** (n - 1)
    
    if zone < 2:
        return zone * one_in_prev + count_one(n - 1, remainder + 1)
    elif zone == 2:
        return 2 * one_in_prev
    else:
        return (zone - 1) * one_in_prev + count_one(n - 1, remainder + 1)

def solution(n, l, r):
    return count_one(n, r) - count_one(n, l - 1)