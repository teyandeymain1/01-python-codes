n = int(input())

list_dic1 = []

for i in range(n):
    list_dic1.append(input().split())

list_dic1 = dict(list_dic1)

list_dic2 = sorted(list_dic1.keys())
list_dic3 = sorted(list_dic1.values())

print(list_dic2)
print(list_dic3)