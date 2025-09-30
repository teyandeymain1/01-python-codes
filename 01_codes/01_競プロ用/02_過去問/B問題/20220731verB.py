def solve():
  n, m = map(int, input().split())
  connect = [[False] * (n+1) for i in range(n+1)]
  print(connect)

  for i in range(m):
    u, v = map(int, input().split())
    connect[u][v] = True
    connect[v][u] = True
    print("connect[u][v]"+str(connect[u][v]))
    print("connect[v][u]"+str(connect[v][u]))

  print(connect)

  ans = 0
  for i in range(1, n+1):
    for j in range(i+1, n+1):
      for k in range(j+1, n+1):
        if connect[i][j] == True and connect[j][k] == True and connect[k][i] == True:
          ans += 1
  return ans 
  
print(solve())