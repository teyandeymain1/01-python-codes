num1 = int(input()) #500
num2 = int(input()) #100
num3 = int(input()) #50
subject = int(input()) #合計

answer = 0
h = 0
i = 0
j = 0

if subject < 100:
    answer = 1

else:
    for h in range(num1 + 1):
        for i in range(num2 + 1):
            for j in range(num3 + 1):
                if (500 * h + 100 * i + 50 * j) == subject:
                    answer += 1

print(answer)