def solution(a, d, included):
    idx=0
    answer=0
    for i in range(len(included)):
        if included[i] == True:
            answer += a+(i*d)
    
    return answer