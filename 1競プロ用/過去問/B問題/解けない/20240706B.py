from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()
inputList2 = make_intList_func()

# 直方体1の範囲
x1_min, x1_max = min(inputList1[0], inputList1[3]), max(inputList1[0], inputList1[3])
y1_min, y1_max = min(inputList1[1], inputList1[4]), max(inputList1[1], inputList1[4])
z1_min, z1_max = min(inputList1[2], inputList1[5]), max(inputList1[2], inputList1[5])

x2_min, x2_max = min(inputList2[0], inputList2[3]), max(inputList2[0], inputList2[3])
y2_min, y2_max = min(inputList2[1], inputList2[4]), max(inputList2[1], inputList2[4])
z2_min, z2_max = min(inputList2[2], inputList2[5]), max(inputList2[2], inputList2[5])

print("1")
print(x1_min, x1_max)
print(y1_min, y1_max)
print(z1_min, z1_max)
print("2")
print(x2_min, x2_max)
print(y2_min, y2_max)
print(z2_min, z2_max)

count = 0
if x1_min < x2_max and x1_max > x2_min:
    count += 1
if y1_min < y2_max and y1_max > y2_min:
    count += 1
if z1_min < z2_max and z1_max > z2_min:
    count += 1

if count == 3:
    print("Yes")
else:
    print("No")