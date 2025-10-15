import sys
readline = sys.stdin.readline
N, = map(int, readline().replace('\n','').replace('\r','').split())
inTuple1 = tuple(map(str, readline().replace('\n','').replace('\r','')))

print(inTuple1)

count = 0
for i in range(N):
    if i <= N-3:
        if inTuple1[i] == "#" and inTuple1[i+2] == "#" and inTuple1[i+1] == ".":
            count += 1
print(count)