from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
valList1 = make_intList_func()

h = valList1[0]
w = valList1[1]

readline = stdin.readline
for i in range(h):
  s= readline()[:-1]
  print(s)
  print(s)