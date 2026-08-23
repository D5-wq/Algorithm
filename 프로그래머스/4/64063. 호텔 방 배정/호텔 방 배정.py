import sys
# 재귀 깊이 제한 해제 (room_number 길이가 최대 20만)
sys.setrecursionlimit(1000000)

def find_empty_room(number, rooms):
    # 해당 방이 비어 있다면 배정 후 다음 후보(number + 1)를 가리키도록 저장
    if number not in rooms:
        rooms[number] = number + 1
        return number
    
    # 이미 배정된 방이라면 연결된 다음 방을 재귀적으로 탐색 (경로 압축 적용)
    empty_room = find_empty_room(rooms[number], rooms)
    rooms[number] = empty_room + 1
    return empty_room

def solution(k, room_number):
    answer = []
    rooms = {} # 방 배정 정보를 담을 딕셔너리
    
    for num in room_number:
        assigned_room = find_empty_room(num, rooms)
        answer.append(assigned_room)
        
    return answer