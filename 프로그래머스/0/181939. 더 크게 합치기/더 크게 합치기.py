def solution(a, b):
    answer = 0
    n1 = int (f"{a}" + f"{b}")
    n2 = int (f"{b}" + f"{a}")
    
    if (n1>n2):
        answer = n1
    else :
        answer = n2
    return answer