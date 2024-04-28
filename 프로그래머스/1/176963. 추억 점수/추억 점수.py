def solution(name, yearning, photo):
    answer = []
    scores = dict(zip(name, yearning))
    
    for people in photo:
        sum = 0
        for person in people:
            if person in name:
                sum += scores[person]
        answer.append(sum)
    return answer