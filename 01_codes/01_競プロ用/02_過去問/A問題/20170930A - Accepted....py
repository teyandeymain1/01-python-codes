#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input()))
    return intList
#------------------------------------------------

list1 = make_intList_func()

print(sum(list1))
