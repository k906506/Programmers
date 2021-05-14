def change(n):
    s = ""
    while n > 1:
        s += str(n%2)
        n //= 2
    s += "1"
    return s

def solution(s):
    countChange = 0
    countRemove = 0
    while 1:
        if len(s) == 1 and s[0] == "1":
            break
        b_s = len(s)
        s = s.replace("0", "")
        a_s = len(s)
        countRemove += b_s - a_s
        countChange += 1
        c = int(len(s))
        s = change(c)
    answer = [countChange, countRemove]
    return answer