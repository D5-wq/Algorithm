from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    # q의 각 시도를 집합(set)으로 변환하여 교집합 연산을 빠르게 수행
    q_sets = [set(query) for query in q]
    
    # 1부터 n까지의 숫자 중 5개를 선택하는 모든 조합 검사
    for comb in combinations(range(1, n + 1), 5):
        comb_set = set(comb)
        
        # 모든 시도 조건(q)과 응답(ans)을 만족하는지 확인
        is_valid = True
        for i in range(len(q)):
            # 교집합의 크기가 시스템 응답과 일치하는지 비교
            if len(comb_set & q_sets[i]) != ans[i]:
                is_valid = False
                break
                
        if is_valid:
            answer += 1
            
    return answer