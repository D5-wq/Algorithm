def solution(record):
    answer = []
    user_dict = {}  
    
    for r in record:
        split_record = r.split() 
        cmd = split_record[0]     
        uid = split_record[1]    
        
        if cmd == "Enter" or cmd == "Change":
            nick = split_record[2]
            user_dict[uid] = nick
            
    for r in record:
        split_record = r.split()
        cmd = split_record[0]
        uid = split_record[1]
        
        if cmd == "Enter":
            answer.append(f"{user_dict[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(f"{user_dict[uid]}님이 나갔습니다.")
            
    return answer