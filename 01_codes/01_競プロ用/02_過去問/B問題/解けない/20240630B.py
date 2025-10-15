from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1].split()))
    return strList
#------------------------------------------------

inputList1 = make_strList_func()

inputStrRow = inputList1[0]
compareStrRow = inputList1[1]

answer = "No"

for i in range(1, len(inputList1[0])):

    print("i=" + str(i))

    for j in range(i):
        
        print("j=" + str(j))
        print(inputStrRow[j::i])

print(answer)