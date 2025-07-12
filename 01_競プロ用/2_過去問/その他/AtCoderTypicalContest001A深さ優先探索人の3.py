import sys
sys.setrecursionlimit(10**9)

h, w = map(int, input().split())
c = [list(input()) for i in range(h)]

d = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def dfs(y, x):

    if c[y][x] == 'g':
        return 'Yes'

    c[y][x] = '#'

    for dy, dx in d:
        ny = y+dy
        nx = x+dx
        if 0 <= ny < h and 0 <= nx < w:
            if c[ny][nx] == '#':
                continue
            res = dfs(ny, nx)
            if res == 'Yes':
                return 'Yes'

    return 'No'

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            ans = dfs(i, j)

print(ans)