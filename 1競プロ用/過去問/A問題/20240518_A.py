
a = int(input())

plant_h = 0
x = 0

while True:
    x += 1
    plant_h = 2 ** x - 1
    if plant_h > a:
        break

print(x)