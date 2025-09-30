def make_dictionary(numOfEle):

    keys_list = []
    values_list = []
    key_tmp = 0
    value_tmp = 1

    for i in range(numOfEle):
        key_tmp = int(input())
        value_tmp += 1

         #---intを変更して辞書の要素の型を変更可/keys_listと交換してもよい---       
        keys_list.append(int(key_tmp))
        values_list.append(int(value_tmp))

    list_dic = []
    list_dic = dict(zip(keys_list, values_list))
    return list_dic
#--------------------------------------------
numOfEle = int(input())

listDic1 = make_dictionary(numOfEle)

print(len(listDic1))