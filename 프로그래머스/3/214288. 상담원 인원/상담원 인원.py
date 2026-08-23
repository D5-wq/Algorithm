import heapq
from itertools import product

def get_wait_time(type_reqs, mentor_cnt):
    """
    [특정 상담 유형에 대한 대기 시간 계산 함수]
    - type_reqs: 해당 유형의 [시작 시각, 상담 시간] 리스트
    - mentor_cnt: 해당 유형에 배치된 멘토 수
    """
    if not type_reqs:
        return 0
    
    # 멘토들의 상담 종료 시각을 저장할 최소 힙 (Min-Heap)
    # 초기 상태: mentor_cnt 명의 멘토가 모두 0분에 상담 종료 상태
    heap = [0] * mentor_cnt
    heapq.heapify(heap)
    
    total_wait_time = 0
    
    for start_time, duration in type_reqs:
        # 가장 먼저 상담이 끝나는 멘토의 종료 시각을 확인
        earliest_end_time = heapq.heappop(heap)
        
        if start_time >= earliest_end_time:
            # 1. 멘토가 놀고 있거나 딱 맞춰 끝난 경우 -> 대기 시간 0
            # 새로운 종료 시각 = (상담 시작 시각 + 상담 시간)
            heapq.heappush(heap, start_time + duration)
        else:
            # 2. 모든 멘토가 상담 중인 경우 -> 대기 발생
            # 기다린 시간 = (가장 빨리 끝나는 멘토의 종료 시각 - 참가자의 요청 시각)
            wait_time = earliest_end_time - start_time
            total_wait_time += wait_time
            
            # 새로운 종료 시각 = (이전 상담 종료 시각 + 상담 시간)
            heapq.heappush(heap, earliest_end_time + duration)
            
    return total_wait_time


def solution(k, n, reqs):
    # 1. 유형별로 상담 요청 분류하기 (1번 유형 ~ k번 유형)
    # req_by_type[c] : c번 상담 유형의 [시작 시간, 상담 시간] 목록
    req_by_type = [[] for _ in range(k + 1)]
    for start, duration, c in reqs:
        req_by_type[c].append((start, duration))
        
    # 2. [전처리] 각 유형별로 (멘토 수 1명 ~ n-k+1명)일 때의 대기 시간을 미리 계산하여 저장
    # wait_time_table[type][mentor_count] = 총 대기시간
    # 멘토 수는 최소 1명부터, 한 유형에 최대로 쏠릴 경우 (n - k + 1)명까지 가능
    max_mentor_per_type = n - k + 1
    wait_time_table = [[0] * (max_mentor_per_type + 1) for _ in range(k + 1)]
    
    for type_idx in range(1, k + 1):
        for mentor_cnt in range(1, max_mentor_per_type + 1):
            wait_time_table[type_idx][mentor_cnt] = get_wait_time(
                req_by_type[type_idx], mentor_cnt
            )

    # 3. 각 유형에 멘토 인원을 나누어 주는 모든 경우의 수 탐색
    # 기본 조건: 모든 유형은 최소 1명의 멘토를 가져야 함.
    # 추가로 배분할 수 있는 멘토 수 = (n - k)명
    remained_mentors = n - k
    min_total_wait_time = float('inf')
    
    # 0명부터 remained_mentors명까지 k개의 유형에 배분하는 모든 조합 생성
    # (예: k=3, remained=2일 때 (1, 1, 0), (2, 0, 0) 등 추가 인원 배정 조합)
    for extra_allocations in product(range(remained_mentors + 1), repeat=k):
        # 추가 배정된 멘토의 총합이 정확히 (n - k)명이어야 유효한 인원 배정
        if sum(extra_allocations) == remained_mentors:
            current_total_wait = 0
            
            for type_idx in range(1, k + 1):
                # 해당 유형의 실제 멘토 수 = 기본 1명 + 추가 배정 인원
                actual_mentor_cnt = 1 + extra_allocations[type_idx - 1]
                current_total_wait += wait_time_table[type_idx][actual_mentor_cnt]
                
            # 최솟값 갱신
            min_total_wait_time = min(min_total_wait_time, current_total_wait)
            
    return min_total_wait_time