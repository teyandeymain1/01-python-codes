from itertools import combinations as c
f = lambda : list(map(int, input().split()))
n, m = f()
n += 1
l = [[] for _ in range(n)]
print(l)
t = [[False] * n for _ in range(n)]
print(t)
for u, v in sorted([f() for _ in range(m)]):
    l[u].append(v)
    t[u][v] = True
print(sum([t[y][z] for x in range(1, n - 1) for y, z in c(l[x], 2)]))