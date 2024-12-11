times = int(input())

result = 0
resultTmp = 0
answerTmp = 0
answer = 0

for i in range(times):
    num = int(input())
    for j in range(2, num+1):
        k = num//j
        if  j <= num:
            resultTmp = (j*(k*(k+1)))/2
        if result <= resultTmp:
            answer = j
            result = resultTmp

    print(answer)