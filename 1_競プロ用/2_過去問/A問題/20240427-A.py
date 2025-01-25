def InputFunc():
    NumList = list(map(int, input().split()))
    return NumList

A = InputFunc()
B = InputFunc()

diffirence = sum(A) - sum(B) + 1

print(diffirence)
