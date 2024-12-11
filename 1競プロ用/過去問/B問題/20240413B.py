import sys
import collections
#------------------整数のリスト-----------------------
def make_int_tuple():
    readline = sys.stdin.readline
    returnData = tuple(map(str, readline()[:-1]))
                  #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#-----------------------------------------------------------------
def make_dict(inList):
    dict = collections.defaultdict(int) 
    for item in inList:
        dict[item] += 1
    return dict
#=====================================================

intuple1 = make_int_tuple()

dict1 = make_dict(intuple1)

dict2 = collections.defaultdict(int)

print(dict1)

for key1 in dict1:
    dict2[dict1[key1]] += 1

answer = "Yes"
for key2 in dict2:
    if dict2[key2] == 0 or dict2[key2] == 2:
        continue 
    else:
        answer ="No"

print(dict2)

print(answer)

