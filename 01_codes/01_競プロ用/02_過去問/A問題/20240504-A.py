def InputFunc():
    NumList = list(map(int, input().split()))
    return NumList

L = InputFunc()

if L[0] <= L[1] or L[0] <= L[2] or L[0] <= L[3]:
    print("No")
elif L[1] <= L[3] and L[3] <= L[2]:
    print("Yes")

elif L[2] <= L[3] and L[3] <= L[1]:
    print("Yes")
else:
    print("No")