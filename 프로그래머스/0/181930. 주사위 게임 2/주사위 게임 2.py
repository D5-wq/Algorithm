def solution(a, b, c):
    # 중복을 제거한 숫자의 개수를 파악합니다.
    count = len({a, b, c})
    
    sum1 = a + b + c
    sum2 = a**2 + b**2 + c**2
    sum3 = a**3 + b**3 + c**3
    
    if count == 3:      # 모두 다른 경우
        return sum1
    elif count == 2:    # 두 개만 같은 경우
        return sum1 * sum2
    else:               # 모두 같은 경우 (count == 1)
        return sum1 * sum2 * sum3