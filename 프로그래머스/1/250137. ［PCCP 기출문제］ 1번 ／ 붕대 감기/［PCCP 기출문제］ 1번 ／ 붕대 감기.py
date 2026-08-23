def solution(bandage, health, attacks):
    cast_time, recovery_per_sec, bonus_recovery = bandage
    max_health = health
    curr_health = health
    last_attack_time = 0

    for attack_time, damage in attacks:
        # 직전 공격 이후 이번 공격 전까지 경과한 시간(초)
        time_diff = attack_time - last_attack_time - 1
        
        if time_diff > 0:
            # 기본 회복량 + 연속 성공 횟수에 따른 추가 회복량
            total_heal = (time_diff * recovery_per_sec) + ((time_diff // cast_time) * bonus_recovery)
            curr_health = min(max_health, curr_health + total_heal)

        # 몬스터의 공격 처리
        curr_health -= damage
        
        # 체력이 0 이하가 되면 캐릭터 사망
        if curr_health <= 0:
            return -1
            
        last_attack_time = attack_time

    return curr_health