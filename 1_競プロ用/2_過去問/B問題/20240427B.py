from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

n=int(input())
inputList1 = make_intList_func()
intList1 = [inputList1[0]]

i=1

while True:
    if len(inputList1)<=1:
        break
    if i==(n-1):
        break

    intList1.append(inputList1[i])

    if not intList1[i-1]==intList1[i]:
        i+=1
    elif intList1[i-1]==intList1[i]:
        n1=intList1.pop(-1)
        n2=intList1.pop(-1)
        inputList1.append(n1+n2)
        print(intList1)
        i+=1
    print(intList1)