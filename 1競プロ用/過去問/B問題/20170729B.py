numOfInput = int(input())

answer = 0

for i in range(numOfInput+1):
    if 2**i <= numOfInput:
        answer = 2**i
print(answer)