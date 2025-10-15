n, m = map(int, input().split())

g = [set() for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].add(v)
    print("u="+str(u)+"v="+str(v))
    print(g)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if j in g[i]:
            ans += len(g[i] & g[j])
            print("g["+str(i)+"]="+str(g[i])+"g["+str(j)+"]="+str(g[j]))
            print("ans="+str(ans))
print(ans)