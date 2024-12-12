import time
#---------------------------------- 行列を表示する---------------------------------------
def print_matrix(inputMatrix):
    print("---答え---")
    for row1 in inputMatrix:         
        print(*row1, sep="")
#------------------------------------------
h, w = map(int, input().split())
G = [input() for _ in range(h)]

start = time.time()
for i in range(h):
    for j in range(w):
        if G[i][j] == "s":
            si, sj = i, j
            
stack = [(si, sj)]
used = [[False] * w for _ in range(h)]
used[si][sj] = True
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while stack:
    i, j = stack.pop()
    for di, dj in directions:
        ni = i + di
        nj = j + dj
        if ni == -1 or ni == h or nj == -1 or nj == w: #枠外
            continue
        if G[ni][nj] == "#" or used[ni][nj]: #壁or探索済
            continue
        if G[ni][nj] == "g": #ゴール到達
            print("Yes")
            exit()
        used[ni][nj] = True
        stack.append((ni, nj))
        print("stack", stack)
        print_matrix(used)
print("No")

