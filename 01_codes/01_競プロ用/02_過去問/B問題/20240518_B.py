n = int(input())

list_dic1 = []

for i in range(n):
    list_dic1.append(input().split())

list_dic1 = dict(list_dic1)
list_dic2 = sorted(list_dic1.keys())

x = 0

for y in list_dic1.values():
    x = (x + int(y))

z = x % n

print(list_dic2[z])