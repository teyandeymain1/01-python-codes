def make_dictionary(numOfEle):

    keys_list = []
    values_list = []
    key_tmp = 0
    value_tmp = 0

    for i in range(numOfEle):
        value_tmp, key_tmp = input().split()

         #---intを変更して辞書の要素の型を変更可/keys_listと交換してもよい---       
        keys_list.append(int(key_tmp))
        values_list.append(int(value_tmp))

    list_dic = []
    list_dic = dict(zip(keys_list, values_list))
    return list_dic

#------------辞書をkeyでソート------------
def sort_dictionary_by_keys(kwargs):
    sorted_keys = sorted(kwargs)
    sorted_dic_by_keys = {a: kwargs[a] for a in sorted_keys}
    return sorted_dic_by_keys
#--------------------------------------------
numOfEle = int(input())

list_dic1 = make_dictionary(numOfEle)

list_dic2 = sort_dictionary_by_keys(list_dic1)

dic1_values_list = list(list_dic1.values())
dic2_values_list = list(list_dic2.values())

list_answer = []
x:int = int(dic2_values_list[0])
y:int = 0
z = ""

for a in dic2_values_list:
    if (int(a) - x) >= 0:
        y = dic1_values_list.index(a)
        list_answer.append(y + 1)
        x = int(a)
    elif (int(a) - x) < 0:
        continue

print(len(list_answer))

s = ""
for i in list_answer:
   s = s + str(i) + " "

print(s)