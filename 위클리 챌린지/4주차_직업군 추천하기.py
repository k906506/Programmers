def solution(table, languages, preference):
    # table은 각 언어별 점수
    # languages는 선택한 언어
    # preference 선택한 언어의 선호도
    # 원하는 것은 점수 * 선호도 가 가장 높은 것
    
    scoreTable = {} # 직업에 따른 점수를 저장할 dict
    result = {} # 직업에 따른 점수 * 선호도를 저장할 dict
    
    for e in table:
        a, b, c, d, e, f = e.split(" ")
        scoreTable[a] = { b : "5", c : "4", d : "3", e : "2", f : "1"}
    
    for e in scoreTable:
        ans = 0
        for index in range(len(languages)):
            if scoreTable[e].get(languages[index]) == None:
                continue
            else :
                ans += int(scoreTable[e][languages[index]]) * preference[index]
        result[e] = ans
    
    result = sorted(result.items(), key = lambda x : (-x[1], x[0]))
    return result[0][0]
