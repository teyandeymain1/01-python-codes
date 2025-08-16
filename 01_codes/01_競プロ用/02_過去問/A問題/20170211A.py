from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

if inputList1[0] == 1 and not inputList1[1] == 1:
    print("Alice")
elif inputList1[1] == 1 and not inputList1[0] == 1:
    print("Bob")
elif inputList1[0] > inputList1[1]:
    print("Alice")
elif inputList1[0] == inputList1[1]:
    print("Draw")
else:
    print("Bob")