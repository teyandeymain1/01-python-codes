#----------------------------------------------
def input_func_int():
    intList = list(map(int, input()))
    return intList
#------------------------------------------------

L = input_func_int()

s = sum(L)

print(int(s))