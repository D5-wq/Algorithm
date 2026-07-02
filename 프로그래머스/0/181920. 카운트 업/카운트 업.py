def solution(start_num, end_num):
    answer = []
    a = start_num
    for i in range(end_num - start_num + 1):
        answer.append(a)
        a += 1
    return answer