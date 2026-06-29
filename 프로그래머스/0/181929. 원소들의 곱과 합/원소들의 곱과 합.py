def solution(num_list):
    answer = 0
    num1=0
    num2=1
    for i in range(len(num_list)):
            a = num_list[i]
            num1 += a
            num2 *= a
                   
    b = num1* num1               
    if b>num2:
            answer=1
    
    return answer