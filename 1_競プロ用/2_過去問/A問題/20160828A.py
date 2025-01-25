nissu = int(input())
nedankawaru = int(input())
saisyonedann = int(input())
hennkounedann = int(input())

nedan = 0

for i in range(nissu):
    if i >= nedankawaru:
        nedan = nedan + hennkounedann
    else:
        nedan = nedan + saisyonedann

print(nedan)