def solution(cards1, cards2, goal):
    a = 0 
    b = 0  
    
    for word in goal:
        if a < len(cards1) and word == cards1[a]:
            a += 1
        elif b < len(cards2) and word == cards2[b]:
            b += 1
        else:
            return "No"
            
    return "Yes"