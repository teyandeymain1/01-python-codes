#----------------------------------------------
def input_func_int():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

L = input_func_int()

if (L[0] * L[1]) % 2 == 0:
    print("Even")
else:
    print("Odd")