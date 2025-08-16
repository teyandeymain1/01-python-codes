N = int(input())

keta = len(str(N))

if keta <= 3:
    print(N)
elif keta <= 4:
    print(str(N)[:3] + "0")
elif keta <= 5:
    print(str(N)[:3] + "00")
elif keta <= 6:
    print(str(N)[:3] + "000")
elif keta <= 7:
    print(str(N)[:3] + "0000")
elif keta <= 8:
    print(str(N)[:3] + "00000")
else:
    print(str(N)[:3] + "000000")