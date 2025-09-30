#-----------------文字のリスト-----------------------
def make_strList_func():
    strList = list(map(str, input().split()))
    return strList
#------------------------------------------------

dict = {"A": 0, "B":3, "C":4, "D":8, "E":9, "F":14, "G":23}

list1 = make_strList_func()

a = str(list1[0])
b = str(list1[1])

print(abs(dict[a] - dict[b]))