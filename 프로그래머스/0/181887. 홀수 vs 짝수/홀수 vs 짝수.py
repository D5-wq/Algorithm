def solution(num_list):
    a = 0
    b = 0
    n= len(num_list)
    for i in range(0,n,2):
        a += num_list[i]
    for i in range(1,n,2):
        b += num_list[i]
        
    if a>b:
        answer=a
    else:
        answer=b
    return answer