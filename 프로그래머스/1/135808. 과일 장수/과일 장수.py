def solution(k, m, score):
    answer = 0
    box = []
    temp = []
    score.sort(reverse=True)
    for i in score:
        temp.append(i)
        if(len(temp)>=m):
            box.append(temp) 
            temp = []
    
    for j in range(len(box)):
        low_score = box[j][-1]
        answer += low_score * m
    return answer