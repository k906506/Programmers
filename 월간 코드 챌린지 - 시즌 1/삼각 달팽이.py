def find(n):
    space = [[0 for _ in range(n+1)] for _ in range(n+1)]
    limit = (n * (n+1))//2
    state = 0 # 0은 아래로, 1은 우측으로, 2는 좌측 상단으로
    top = 1
    bottom = n
    left = 1
    right = 0
    value = 1
    while value <= limit:
        if state == 0: # 아래로 내려가는 경우
            for j in range(top, bottom+1):
                space[j][left] = value
                value += 1
            top += 1
            left += 1
            state = 1
        elif state == 1: # 우측으로 가는 경우
            for j in range(left, bottom - right + 1):
                space[bottom][j] = value
                value += 1
            bottom -= 1
            state = 2
        else:
            for j in range(bottom, top-1, -1):
                space[j][j-right] = value
                value += 1
            right += 1
            top += 1
            state = 0

    answer = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            answer.append(space[i][j])

    return answer

def solution(n):
    answer = []
    answer = find(n)
    return answer