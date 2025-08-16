#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

inputList = make_intList_func()

list1 = make_intList_func()

kiraiList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(inputList[0], 100000):
    counter = 0
    for j in list(list1):
        if str(j) in str(i):
            break
        else:
            counter +=1
            
    if counter == len(list1):
        print(i)
        break