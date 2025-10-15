numOfPower = int(input())

answer = 1

if numOfPower == 0:
    answer = 0

for i in range(1, numOfPower+1):
    answer = answer*i%((10**9)+7)

print(answer)