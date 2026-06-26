def solution(n):
    answer = 0
    if n % 2 == 1:                      # 홀수면
        for i in range(1, n + 1, 2):    # 1, 3, 5, ... , n
            answer += i                 # 그냥 더하기
    else:                               # 짝수면
        for i in range(2, n + 1, 2):    # 2, 4, 6, ... , n
            answer += i * i             # 제곱해서 더하기
    return answer