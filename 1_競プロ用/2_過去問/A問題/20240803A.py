

yearStr = str(input())

print(int(yearStr[2:4]))

if int(yearStr[2:4])%4 != 0:
    print("365")
elif int(yearStr[2:4])%4 == 0 and int(yearStr)%100 !=0:
    print("366")
elif int(yearStr[2:4])%4 == 0 and int(yearStr)%400 !=0:
    print("365")
elif int(yearStr[2:4])%4 == 0 and int(yearStr)%400 ==0:
    print("366")