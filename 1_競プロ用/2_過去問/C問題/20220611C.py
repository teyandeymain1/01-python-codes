from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

X = inputList1[0]
A = inputList1[1]
D = inputList1[2]
N = inputList1[3]

numSeqresList = [0]*N

for i in range(N):
    numSeqresList[i] = A + i*D

miniTmp = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
miniAnswer = 0

for j in range(N):
    if abs(X - numSeqresList[j]) <= miniTmp:
        miniAnswer = numSeqresList[j]
        miniTmp = abs(X - numSeqresList[j])

print(miniAnswer)

answer = 0

if miniAnswer == 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    print(answer)
elif miniAnswer >= 0 and not miniAnswer == 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    answer = abs(abs(X) - abs(miniAnswer))
    print(answer)
elif miniAnswer < 0 and not miniAnswer == 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    answer = abs(abs(X) + abs(miniAnswer))
    print(answer)
