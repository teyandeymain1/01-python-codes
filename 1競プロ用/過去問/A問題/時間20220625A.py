from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

valList = make_intList_func()

alfbList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

answerRow = ""

for i in range(26):
    answerRow = answerRow + alfbList[i]*valList[0]

X = valList[1]

print(answerRow[(valList[1]-1):(valList[1])])