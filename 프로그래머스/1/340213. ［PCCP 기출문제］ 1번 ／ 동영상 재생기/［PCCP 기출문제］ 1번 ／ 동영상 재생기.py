def to_seconds(time_str):
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def solution(video_len, pos, op_start, op_end, commands):
    v_len = to_seconds(video_len)
    p = to_seconds(pos)
    o_start = to_seconds(op_start)
    o_end = to_seconds(op_end)
    
    if o_start <= p <= o_end:
        p = o_end
        
    for cmd in commands:
        if cmd == "prev":
            p = max(0, p - 10)
        elif cmd == "next":
            p = min(v_len, p + 10)
            
        if o_start <= p <= o_end:
            p = o_end
            
    return f"{p // 60:02d}:{p % 60:02d}"