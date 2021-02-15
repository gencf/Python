def marble_game(l):
    p = []
    score = 0
    w_score = 0
    index = 0
    for i in l:
        for j in i:
            if j == 'silver':
                score += 2 
            elif j == 'white':
                score += 3             
            elif j == 'red':
                score += 5
            elif j == 'black':
                continue
            else:
                score += 1
        p.append(score)
        score = 0
    for i in range(len(p)):
        if p[i] > w_score:
            w_score = p[i]
            index = i
    return [l[index], w_score]
            
            
marble_game([['yellow', 'yellow', 'red'], ['red', 'red', 'yellow']])       
marble_game([['silver', 'red', 'silver'], ['red', 'black', 'red']])
marble_game([['blue', 'blue', 'red', 'white', 'white'], ['white', 'silver', 'white', 'red', 'yellow'], ['silver', 'red', 'white', 'yellow', 'white']])