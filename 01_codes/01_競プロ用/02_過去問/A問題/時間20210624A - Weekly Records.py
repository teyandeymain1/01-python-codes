#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

n = int(input())
list0 = [0]
list1 = list0 + make_intList_func()

answerList = []
answerSum = 0

for i in range(1, len(list1)):
    if i%7 == 0:
        answerSum = answerSum + list1[i]
        answerList.append(answerSum)
        answerSum = 0
    else:
        answerSum = answerSum + list1[i]

print(*answerList)