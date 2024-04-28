def solution(n, m, section):
    answer = 1
    prev = section[0]
    
    for i in range(1, len(section)):
        if(section[i] - prev >= m):
            prev = section[i]
            answer+=1
        else:
            continue
    return answer