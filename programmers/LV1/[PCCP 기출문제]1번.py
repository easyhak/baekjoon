def solution(video_len, pos, op_start, op_end, commands):
    
    video_minute, video_second = map(int, video_len.split(":"))
    start_minute, start_second = map(int, pos.split(":"))
    op_start_minute, op_start_second = map(int, op_start.split(":"))
    op_end_minute, op_end_second = map(int, op_end.split(":"))
    ##
    total_length = get_total_seconds(video_minute, video_second)
    now = get_total_seconds(start_minute, start_second)
    start = get_total_seconds(op_start_minute, op_start_second)
    end = get_total_seconds(op_end_minute, op_end_second)
    
    if (start <= now <= end):
        now = end
    for x in commands:
        if (x == "next"):
            now = now + 10     
        else:
            now = now - 10
        if now < 0:
            now = 0
        elif now > total_length:
            now = total_length
        if start <= now <= end:
            now = end
        
    
    now_min = str(now // 60)
    now_sec = str(now % 60)
    if (len(now_min) == 1):
        now_min = "0"+now_min
    if (len(now_sec) == 1):
        now_sec = "0"+now_sec
    result = now_min + ":" + now_sec
    return result

def get_total_seconds(minute, second):
    return minute*60 + second


