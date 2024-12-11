x=int(input())

answer=0

if x%100==0:
    answer = 100
elif not x%100==0:
    answer = 100-(x%100)

print(answer)