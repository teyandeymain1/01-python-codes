n = int(input())
a = list(map(int, input().split()))
cnt = [0 for _ in range(3 * n)] #for _でループの変数を省略
ans = []
for i in a:
    cnt[i] += 1
    if cnt[i] == 2:
        ans.append(i)
print(*ans) #アスタリスク+リストをスペースありの横列で表示