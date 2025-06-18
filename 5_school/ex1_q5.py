from random import *

# if (conditional) statements randint version 

v0 = 20000000000000000
v1 = 0
v2 = v0

count = 0
while v1 <= v2:
    rand = randint(v1, v2)
    if rand * rand > v0:
        v2 = rand - 1 # 最大値を減らして範囲を狭める
        #print("flag1")
        #print("rand", rand)
        #print("v2", v2)
    else:
        v1 = rand + 1 # 最小値を増やして範囲を狭める
        #print("flag2")
        #print("rand", rand)
        #print("v1", v1)
    count += 1
    #print("count:", count)
print('sr(', v0, ') = ', v1)
#print("count:", count)