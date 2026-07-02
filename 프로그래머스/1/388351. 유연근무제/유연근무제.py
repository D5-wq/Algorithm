def solution(schedules, timelogs, startday):
    answer = 0  
    
    for i in range(len(schedules)):
        limit_time = schedules[i] + 10
        
        if limit_time % 100 >= 60:
            limit_time += 40
            
        is_perfect = True  
        
        for j in range(7):
            current_day = (startday - 1 + j) % 7
            
            if current_day == 5 or current_day == 6:
                continue
                
            if timelogs[i][j] > limit_time:
                is_perfect = False
                break
        
        if is_perfect:
            answer += 1
            
    return answer