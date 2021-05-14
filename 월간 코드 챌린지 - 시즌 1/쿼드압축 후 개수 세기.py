count = [0, 0]

def find(x, y, size, arr):
    element = arr[x][y]
    check = True
    if size == 1:
        count[element] += 1
        return
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != element:
                check = False
    if check == True:
        count[element] += 1
    else:
        find(x, y, size // 2, arr)
        find(x, y + size // 2, size // 2, arr)
        find(x + size // 2, y, size // 2, arr)
        find(x + size // 2, y + size // 2, size // 2, arr)

def solution(arr):
    size = len(arr[0])
    find(0, 0, size // 2, arr)
    find(0, size // 2, size // 2, arr)
    find(size // 2, 0, size // 2, arr)
    find(size // 2, size // 2, size // 2, arr)

    return count