def solution(players, callings):
    # 1. 선수의 {이름: 현재등수(인덱스)}를 저장하는 딕셔너리를 미리 만듭니다.
    # 예: {"mumu": 0, "soe": 1, "poe": 2 ...}
    player_indices = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        # 2. 딕셔너리를 이용해 불린 선수의 인덱스를 '즉시' 찾습니다. (O(1))
        current_idx = player_indices[calling]
        front_idx = current_idx - 1
        front_player = players[front_idx] # 바로 앞 선수 이름
        
        # 3. 실제 players 배열에서 두 선수의 위치를 교환합니다.
        players[front_idx], players[current_idx] = players[current_idx], players[front_idx]
        
        # 4. 등수가 바뀌었으니 딕셔너리의 위치 정보도 둘 다 업데이트해 줍니다.
        player_indices[calling] = front_idx
        player_indices[front_player] = current_idx
        
    return players