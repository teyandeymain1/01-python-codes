#----------------------------------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

list1 = make_intList_func()
list2 = [1,2,3]

if list1[0] == list1[1]:
    print("-1")
else:
    for i in range(len(list2)):
        if not list1[0] == list2[i] and not list1[1] == list2[i]:
            print(list2[i])