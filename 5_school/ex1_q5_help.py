# if (conditional) statements randint version 

v0 = 20000000000000000
v1 = 0
v2 = v0

count = 0
while v1 != v2:
    if (v2-v1)%2 == 0:
        v3 = v1+(v2-v1)//2
        #print("flag1")
        #print("v3", v3)
    else:
        v3 = v1+(v2-v1)//2+1
        #print("flag2")
        #print("v3", v3)
    if v3*v3 > v0:
        v2 = v3-1
        #print("flag3")
        #print("v3", v3)
        #print("v2", v2)
    else:
        v1 = v3
        #print("flag4")
        #print("v3", v3)
        #print("v1", v1)
    count += 1
print('sr(', v0, ') = ', v1)
print("count:", count)