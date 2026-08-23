def solution(n):
    answer = 0
    
    while n > 0:
        remainder = n % 3     
        answer = answer * 3 + remainder 
        n = n // 3
        
    return answer