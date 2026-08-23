def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning))
    
    answer = []

    for p in photo:
        total_score = 0
        for person in p:
            total_score += score_dict.get(person, 0)
        answer.append(total_score)
        
    return answer