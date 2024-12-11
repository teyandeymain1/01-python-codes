#-----------------文字のリスト-----------------------
def make_strList_func():
    strList = list(map(str, input()))
    return strList
#------------------------------------------------

list1 = make_strList_func()

answer = 0

if list1 == ["R", "R", "R"]:
    answer = 3
elif list1 == ["R", "R", "S"] or list1 == ["S", "R", "R"]:
    answer = 2
elif list1 == ["R", "S", "S"] or list1 == ["S", "S", "R"] or  list1 == ["R", "S", "R"] or list1 == ["S", "R", "S"]:
    answer = 1

print(answer)