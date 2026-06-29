def solution(my_string, n):
    answer = ''
    answer = my_string[-n:-1] + my_string[-1]
    return answer