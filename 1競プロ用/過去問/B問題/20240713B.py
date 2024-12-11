from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

a = make_intList_func()
b = make_intList_func()
c = make_intList_func()

distance1 = (a[0]-b[0])**2 + (a[1]-b[1])**2
distance2 = (b[0]-c[0])**2 + (b[1]-c[1])**2
distance3 = (c[0]-a[0])**2 + (c[1]-a[1])**2

print(distance1)
print(distance2)
print(distance3)

if (distance1 + distance2) == distance3:
    print("Yes")
elif (distance2 + distance3) == distance1:
    print("Yes")
elif (distance3 + distance1) == distance2:
    print("Yes")
else:
    print("No")