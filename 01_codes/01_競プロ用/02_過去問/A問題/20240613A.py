number1 = int(input())

count=0
answer=0

for i in range(1, number1+1, 2):
    for j in range(1, i+1):
        if i % j ==0:
            count+=1
    if count == 8:
        answer+=1
    count=0

print(answer)