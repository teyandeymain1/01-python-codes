from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

valList1 = make_intList_func()

inputList1 = make_intList_func()

inputList1.append("?")

people = valList1[0]
processTime = valList1[1]

for i in range(0, people):
    if i == 0:
        waitTime = inputList1[i] + processTime
        print(waitTime)
    elif inputList1[i] - inputList1[i-1] <= processTime:
        waitTime = waitTime + processTime
        print(waitTime)
    elif inputList1[i] - inputList1[i-1] > processTime:
         waitTime = inputList1[i] + processTime
         print(waitTime)