from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

inputListA = make_strList_func()
inputListB = make_strList_func()
inputListC = make_strList_func()

turn = "a"
countA = 0
countB = 0
countC = 0

while True:
    if turn == "a":
        if countA == len(inputListA):
            answer = "A"
            break
        turn = inputListA[countA]        
        countA += 1

    if turn == "b":
        if countB == len(inputListB):
            answer = "B"
            break 
        turn = inputListB[countB]
        countB += 1

    if turn == "c":
        if countC == len(inputListC):
            answer = "C"
            break
        turn = inputListC[countC]  
        countC += 1



print(answer)