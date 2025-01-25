times = int(input())

list1 = list() 

for i in range(times):
    list1.append(str(input()))

answer = "No"

for j in range(0, times):
    for k in range(0, times):
        if j == k:
            continue
        else:
            resultStr = list1[k] + list1[j]
            if list(resultStr) == list(reversed(resultStr)):
                answer = "Yes"

print(answer)