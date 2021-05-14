def change(n):
    a = ""
    while n > 1:
        if n == 2:
            break
        a += str(n%3)
        n //= 3
    if n == 1:
        a += "1"
    else:
        a += "2"
    return a[::-1]

def rechange(n):
    ans = 0
    index = 0
    for i in range(len(n)):
        if n[i] != 0:
            ans += int(n[i]) * 3 ** index
        index += 1
    return ans

def solution(n):
    three = change(n)
    answer = rechange(three)
    return answer