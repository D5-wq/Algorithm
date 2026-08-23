def solution(info, n, m):
    INF = float('inf')
    dp = {0: 0}
    
    for a_trace, b_trace in info:
        next_dp = {}
        for b_sum, a_sum in dp.items():
            
            new_a = a_sum + a_trace
            if new_a < n:
                if b_sum not in next_dp or new_a < next_dp[b_sum]:
                    next_dp[b_sum] = new_a
      
            new_b = b_sum + b_trace
            if new_b < m:
                if new_b not in next_dp or a_sum < next_dp[new_b]:
                    next_dp[new_b] = a_sum
                    
        dp = next_dp
    
        if not dp:
            return -1
            
    ans = min(dp.values())
    return ans if ans < n else -1