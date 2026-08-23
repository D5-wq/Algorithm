def solution(diffs, times, limit):
    
    def get_total_time(level):
        total = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1] if i > 0 else 0
            
            if diff <= level:
                total += time_cur
            else:
                mistakes = diff - level
                total += mistakes * (time_cur + time_prev) + time_cur
                
            
            if total > limit:
                return total
        return total

    start = 1
    end = max(diffs)
    answer = end


    while start <= end:
        mid = (start + end) // 2
        
 
        if get_total_time(mid) <= limit:
            answer = mid      
            end = mid - 1      
        else:
            start = mid + 1    

    return answer