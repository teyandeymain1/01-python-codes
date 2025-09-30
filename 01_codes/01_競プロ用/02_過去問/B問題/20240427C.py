from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#---------------昇順でリストをソート---------------
def sort_list_asc_func(list):
    list = sorted(list, reverse=False) #昇順
    return list
#-------------------------------------------------

inputList0 = make_intList_func()

n = inputList0[1]
q=inputList0[0]

inputList1 = make_intList_func()
inputList1 = sort_list_asc_func(inputList1)
inputList2 = sort_list_asc_func(inputList1)

for i in range(n-1):
    if not inputList1[i]==inputList1[i+1]:
        continue
    elif inputList1[i]==inputList1[i+1]:
        print(i)
        inputList2.pop()
        inputList2.pop()
    print(inputList2)

answer=q-len(inputList1)

print(answer)